from django.db import models
from django.contrib.auth.models import User
from edumanage.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    institution = models.ForeignKey(Institution)
    is_social_active = models.BooleanField(default=False)
    
    class Meta:
       permissions = (
                ("overview", "Can see registered user and respective institutions"),
            )
    
    def __unicode__(self):
        return "%s:%s" %(self.user.username, self.institution)

