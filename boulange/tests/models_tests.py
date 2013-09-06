from django.test import TestCase

from boulange.models import InventoryItem, OnHandInventoryItem

class InventoryItemTestCase(TestCase):
	def setUp(self):
		InventoryItem.objects.create(name='Chocolate Croissant',case_size=32)
		InventoryItem.objects.create(name='Birthday Cake Pop',inner_pack=True,inner_pack_size=4,case_size=56)

	def test_string_representation(self):
		chct = InventoryItem.objects.get(name='Chocolate Croissant')
		self.assertEqual(str(chct),'Chocolate Croissant')

class OnHandInventoryItemTestCase(TestCase):
	def setUp(self):
		chct = InventoryItem.objects.create(name='Chocolate Croissant',case_size=32)
		bcp = InventoryItem.objects.create(name='Birthday Cake Pop',inner_pack=True,inner_pack_size=4,case_size=56)
		bct = InventoryItem.objects.create(name='Butter Croissant', case_size=32)
		OnHandInventoryItem.objects.create(item=chct,cases=2)
		OnHandInventoryItem.objects.create(item=bcp,inner_packs=3,cases=1)
		OnHandInventoryItem.objects.create(item=bct,eaches=30,cases=1)

	def test_string_representation(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		self.assertEqual(str(chct),'Chocolate Croissant')

	def test_eaches_calculation(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		self.assertEqual(chct.eaches_on_hand(),64)

		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		self.assertEqual(bcp.eaches_on_hand(), 68)

	def test_inner_packs_calculation(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		self.assertEqual(chct.inner_packs_on_hand(), 0)

		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		self.assertEqual(bcp.inner_packs_on_hand(), 17)

	def test_pastry_pull_no_case(self):
		bct = OnHandInventoryItem.objects.get(item__name='Butter Croissant')
		bct.pull(15)
		self.assertEqual(bct.cases, 1)
		self.assertEqual(bct.eaches, 15)
		self.assertEqual(bct.eaches_on_hand(), 47)

	def test_pastry_pull_open_case(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		chct.pull(15)
		self.assertEqual(chct.cases, 1)
		self.assertEqual(chct.eaches_on_hand(), 49)

	def test_inner_pack_pastry_pull_no_case(self):
		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		bcp.pull(12)
		self.assertEqual(bcp.cases, 1)
		self.assertEqual(bcp.inner_packs, 0)

	def test_inner_pack_pastry_pull_open_case(self):
		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		bcp.pull(16)
		self.assertEqual(bcp.cases, 0)
		self.assertEqual(bcp.inner_packs, 13)
		self.assertEqual(bcp.inner_packs_on_hand(), 13)

	def test_inner_pack_uneven_pull(self):
		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		with self.assertRaises(NotImplementedError):
			bcp.pull(5)

	def test_pastry_overpull(self):
		chct = OnHandInventoryItem.objects.get(item__name='Chocolate Croissant')
		with self.assertRaises(ArithmeticError):
			chct.pull(100)

	def test_inner_pack_overpull(self):
		bcp = OnHandInventoryItem.objects.get(item__name='Birthday Cake Pop')
		with self.assertRaises(ArithmeticError):
			bcp.pull(100)
