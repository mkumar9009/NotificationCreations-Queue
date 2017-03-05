from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator,validate_integer


# Create your models here.

class UserType(models.Model):
	name = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name_plural = 'User Type'

	def __str__(self):
		return str(self.name)


class Users(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	username = models.CharField(max_length=50,unique=True)
	email_address = models.EmailField(max_length=80,unique=True)
	phoneno = models.CharField(max_length=15,validators=[MaxLengthValidator(14), MinLengthValidator(10), validate_integer])
	user_img = models.ImageField(upload_to='image/user/',blank=True,null=True)
	added_on = models.DateTimeField(auto_now_add=True)
	lastvisit_date = models.DateTimeField()
	address = models.CharField(max_length=200,blank=True,null=True)
	user_type = models.ForeignKey(UserType)

	class Meta:
		verbose_name_plural = 'Users'


	def __str__(self):
		return str(self.email_address)



class Notifications(models.Model):
	BROADCAST =0
	USER = 1
	TYPE_CHOICES = (
			(BROADCAST,'Admin'),
			(USER,'Individual'),
		)
	
	notifications_type = models.SmallIntegerField(choices=TYPE_CHOICES,default=BROADCAST)
	created = models.DateTimeField(auto_now_add=True)
	deliver_time = models.DateTimeField()
	content = models.CharField(max_length=300)
	user_type = models.ForeignKey(UserType)
	
	class Meta:
		verbose_name_plural = 'Notifications'
