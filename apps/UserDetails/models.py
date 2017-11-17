from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[^\W_]+(-[^\W_]+)?$', re.U)

class UserManager(models.Manager):
    def register_validator(self,postData):
        #Initialize empty array for errors 
        errors = [] 
        # check first name and last name length
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors.append("User name/last name should be more than 2 characters")
        # check first_name and last_name for valid characters
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append("User name/last name should contains only letters")  
        # check email with Email_REgex
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("Invalid email format")
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("email already in use") 
        if not errors:
                # add a new user
                new_user = self.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    email=postData['email']
                )
                return new_user
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
	      return "User object:: \nfirst_name: {}, \nlast_name: {}, \n email: {} ".format(self.first_name, self.last_name, self.email)

