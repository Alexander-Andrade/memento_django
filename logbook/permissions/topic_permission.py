from rest_framework.permissions import BasePermission

from logbook.models import Bookmark


class TopicPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return Bookmark.objects.get(pk=view.kwargs['bookmark_pk']).user_id == request.user.id
