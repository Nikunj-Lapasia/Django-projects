from django.db import models

class Jobs(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Jobs'