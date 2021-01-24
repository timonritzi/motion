from django.contrib import admin

# Register your models here.
from apps.comments.models import Comments

admin.site.register(Comments)