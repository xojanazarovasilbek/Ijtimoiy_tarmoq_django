from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = True
    list_display = ['body']

admin.site.register(Notification)
admin.site.register(View)
