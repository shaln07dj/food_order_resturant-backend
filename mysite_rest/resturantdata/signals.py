from django.db.models.signals import pre_save
from django.contrib.auth.models import User

def updateUser(sender,instance,**kwargs):
    print("Signal Triggered")
    user=instance
    if user.email !='':
        if user.username =='':
            user.username=user.email

pre_save.connect(updateUser,sender=User)