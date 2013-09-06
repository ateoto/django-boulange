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

	def inner_packs_on_hand(self):
		if self.item.inner_pack:
			return (self.inner_packs + (self.cases * (self.item.case_size / self.item.inner_pack_size)))
		else:
			return 0

	def pull(self, eaches_pulled):
		if self.item.inner_pack:
			if eaches_pulled % self.item.inner_pack_size == 0:
				inner_packs_pulled = eaches_pulled / self.item.inner_pack_size
				if inner_packs_pulled <= self.inner_packs_on_hand():
					if inner_packs_pulled <= self.inner_packs:
						self.inner_packs -= inner_packs_pulled
					else:
						self.cases -= 1
						self.inner_packs += self.item.case_size / self.item.inner_pack_size
						self.inner_packs -= inner_packs_pulled
				else:
					raise ArithmeticError('Not enough inventory to support pull.')
			else:
				raise NotImplementedError('Please pull in multiples of inner packs')

		else:
			if self.eaches_on_hand() < eaches_pulled:
				raise ArithmeticError('Not enough inventory to support pull.')
			else:
				if self.eaches >= eaches_pulled:
					self.eaches -= eaches_pulled
				else:
					if self.cases > 0:
						self.cases -= 1
						self.eaches = self.item.case_size
						self.eaches -= eaches_pulled
