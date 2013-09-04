from django.test import LiveServerTestCase
from selenium import webdriver

from boulange import models

class NewVisitorTest(LiveServerTestCase):
	fixtures = ['test_inventoryitem.json']

	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Firefox()
		cls.browser.implicitly_wait(3)
		super(NewVisitorTest, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		cls.browser.quit()

	def test_can_see_inventory_list(self):
		self.browser.get('%s%s' % (self.live_server_url, '/boulange/inventory/'))

		list_items = self.browser.find_elements_by_tag_name('li')

		for inventory_item in models.InventoryItem.objects.all():
			self.assertTrue(
				any(list_item.text == inventory_item.name for list_item in list_items)
			)