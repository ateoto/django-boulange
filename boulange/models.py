from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class InventoryItem(models.Model):
	name = models.CharField(max_length=70)
	inner_pack = models.BooleanField(default=False)
	inner_pack_size = models.IntegerField()
	case_size = models.IntegerField()

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class OnHandInventoryItem(models.Model):
	item = models.ForeignKey(InventoryItem)
	eaches = models.IntegerField()
	inner_packs = models.IntegerField()
	cases = models.IntegerField()

	def __str__(self):
		return self.item.name
