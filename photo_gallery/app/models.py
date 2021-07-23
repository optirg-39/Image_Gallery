from django.db import models

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length = 100, null = False, blank = False)

	def __str__(self):
		return self.name 

	class Meta:
		db_table = 'Tag'

class PhotoImage(models.Model):
	tag = models.ManyToManyField(Tag, related_name="photo")
	address = models.ImageField(null = False, blank = False)
	description = models.TextField()

	def __str__(self):
		return self.description 

	class Meta:
		db_table = 'PhotoImage'