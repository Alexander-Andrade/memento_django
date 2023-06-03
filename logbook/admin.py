from django.contrib import admin
from .models import Bookmark, Event, Note, Entry, Topic


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', )


class EventAdmin(admin.ModelAdmin):
    list_display = ('description', )


class NoteAdmin(admin.ModelAdmin):
    list_display = ('description', )


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', )


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Topic, TopicAdmin)
