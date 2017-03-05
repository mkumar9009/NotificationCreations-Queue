from django.contrib import admin
from testapp.models import Users,Notifications,UserType
# Register your models here.

@admin.register(Users)
class Users(admin.ModelAdmin):
	list_display = ('firstname','lastname','email_address')
	search_fields = ['email_address']

@admin.register(Notifications)
class Notifications(admin.ModelAdmin):
	list_display = ('notifications_type','created','content', 'user_type')

@admin.register(UserType)
class UserType(admin.ModelAdmin):
	list_display = ('name',)