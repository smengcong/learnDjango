from django.contrib import admin
from app02 import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.UserToTag)
admin.site.register(models.Tag)