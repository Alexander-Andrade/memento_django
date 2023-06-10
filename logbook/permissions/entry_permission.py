from rest_framework.permissions import BasePermission

from logbook.models import Topic


class EntryPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return Topic.objects.get(pk=view.kwargs['topic_pk']).user_id == request.user.id
