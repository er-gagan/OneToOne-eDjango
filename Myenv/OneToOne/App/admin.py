from django.contrib import admin
from .models import Song,Singer
# Register your models here.
admin.site.register(Singer)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'singer', 'song_publish_date']