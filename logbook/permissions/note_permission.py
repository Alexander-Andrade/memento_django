from rest_framework.permissions import BasePermission

from logbook.models import Entry


class NotePermission(BasePermission):
    def has_permission(self, request, view):
        return self.is_user_entry(request, view)

    def has_object_permission(self, request, view, obj):
        return self.is_user_entry(request, view)

    def is_user_entry(self, request, view):
        return Entry.objects.get(pk=view.kwargs['entry_pk']).user_id == request.user.id
