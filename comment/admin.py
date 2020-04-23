from django.contrib import admin
from .models import ItemComment, ItemReplayComment


# Register your models here.

admin.site.register(ItemComment)
admin.site.register(ItemReplayComment)
