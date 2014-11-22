from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserProfile(models.Model):
	username = models.OneToOneField(User)
	user_phone = models.CharField(max_length=12)
	avatar = models.ImageField(upload_to='userprofiles', blank=True)
	calification = models.SmallIntegerField(default=3)

	def __unicode__(self):
		return self.username.username

	def Foto_Avatar(self):
		return """
				<img src="%s" height="100" widht="42"></img>
				""" % (self.avatar.url)

	Foto_Avatar.allow_tags = True