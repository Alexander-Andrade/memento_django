# from rest_framework import routers as rest_routers
from django.urls import include, path
from rest_framework_nested import routers

from .views import BookmarkView, TopicNestedView, TopicView, EntryNestedView, EntryView, NoteNestedView

# api_router = rest_routers.DefaultRouter()
# api_router.register(r'bookmarks', BookmarkView, 'bookmark')

bookmarks_router = routers.SimpleRouter()
bookmarks_router.register(r'bookmarks', BookmarkView, 'bookmark')

topics_nested_router = routers.NestedSimpleRouter(bookmarks_router, r'bookmarks', lookup='bookmark')
topics_nested_router.register(r'topics', TopicNestedView, basename='bookmark-topics')


topics_router = routers.SimpleRouter()
topics_router.register(r'topics', TopicView, 'topic')

entries_nested_router = routers.NestedSimpleRouter(topics_router, r'topics', lookup='topic')
entries_nested_router.register(r'entries', EntryNestedView, basename='topic-entries')


entries_router = routers.SimpleRouter()
entries_router.register(r'entries', EntryView, 'entry')

notes_nested_router = routers.NestedSimpleRouter(entries_router, r'entries', lookup='entry')
notes_nested_router.register(r'notes', NoteNestedView, basename='entry-notes')


urlpatterns = [
    path(r'', include(bookmarks_router.urls)),
    path(r'', include(topics_nested_router.urls)),

    path(r'', include(topics_router.urls)),
    path(r'', include(entries_nested_router.urls)),

    path(r'', include(entries_router.urls)),
    path(r'', include(notes_nested_router.urls)),
]
