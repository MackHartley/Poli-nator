from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	upvotes = models.IntegerField(default=0)
	#photo url field

	def __str__(self):
		return 'answer: %s, upvotes: %s' % (self.text, self.upvotes)