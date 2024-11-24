from django.contrib import admin
from . import models

admin.site.site_header = "RZA Administration Portal"

# Register your models here.

admin.site.register(models.Account)