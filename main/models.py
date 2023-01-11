from django.db import models

# Create your models here.
class ToDoList(models.Model):
	name = models.CharField(max_length = 200)

	def _str_(self):
		return self.name

class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
	text = models.CharField(max_length = 300)
	complete = models.BooleanField()


	def _str_(self):
		return self.text


class Questions(models.Model):
	WhichLand = models.CharField(max_length=200)

	def _str_(self):
		return self.WhichLand

class Features(models.Model):
	lands = models.ForeignKey(Questions, on_delete = models.CASCADE)
	features = models.CharField(max_length = 300)
	clicked = models.BooleanField()


	def _str_(self):
		return self.features







