from django.contrib import admin
from UserManagement.models import*
# Register your models here.

class userInfo(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'cnic', 'address', 'phoneNumber', 'gender')
    
admin.site.register(User, userInfo)