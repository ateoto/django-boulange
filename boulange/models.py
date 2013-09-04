from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class InventoryItem(models.Model):
	name = models.CharField(max_length=70)
	inner_pack = models.BooleanField(default=False)
	inner_pack_size = models.IntegerField(default=0,blank=True)
	case_size = models.IntegerField()

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class OnHandInventoryItem(models.Model):
	item = models.ForeignKey(InventoryItem)
	eaches = models.IntegerField(default=0)
	inner_packs = models.IntegerField(default=0)
	cases = models.IntegerField(default=0)

	def __str__(self):
		return self.item.name

	def eaches_on_hand(self):
		return self.eaches + (self.inner_packs * self.item.inner_pack_size) + (self.cases * self.item.case_size)