from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(User):
	"""docstring for UserProfile"""
	facebook_uid = models.CharField(max_length=20, unique=True, db_index=True)
	accesstoken = models.CharField(max_length=1024)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
