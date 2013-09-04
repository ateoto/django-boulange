from django.test import TestCase

from boulange.models import InventoryItem, OnHandInventoryItem

class InventoryItemTestCase(TestCase):
	def setUp(self):
		InventoryItem.objects.create(name='Chocolate Croissant',case_size=32)
		InventoryItem.objects.create(name='Birthday Cake Pop',inner_pack=True,inner_pack_size=4,case_size=56)

class OnHandInventoryItemTestCase(TestCase):
	def setUp(self):
		chct = InventoryItem.objects.create(name='Chocolate Croissant',case_size=32)
		bcp = InventoryItem.objects.create(name='Birthday Cake Pop',inner_pack=True,inner_pack_size=4,case_size=56)
		OnHandInventoryItem.objects.create(item=chct,cases=2)
		OnHandInventoryItem.objects.create(item=bcp,inner_packs=3,cases=1)

	def test_eaches_calculation(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		self.assertEqual(chct.eaches_on_hand(),64)

		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		self.assertEqual(bcp.eaches_on_hand(), 68)

	def test_pastry_pull(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		chct.pull(15)
		self.assertEqual(chct.cases, 1)
		self.assertEqual(chct.eaches_on_hand(), 49)

	def test_pastry_pull_overpull(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		with self.assertRaises(ArithmeticError):
			chct.pull(100)