from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100,default='')
	pub_date = models.DateTimeField(default = datetime.datetime.now)
	image = models.ImageField(upload_to='images/')
	summary = models.TextField()

	def __str__(self):
		return self.title

	def summary_short(self):
		return self.summary[:75]

	def date_strip(self):
		return self.pub_date.strftime('%b %e %Y')	