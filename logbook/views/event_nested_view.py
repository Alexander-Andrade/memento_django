from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from ..serializers import EventSerializer
from ..models import Event
from ..permissions import NotePermission


class EventNestedView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, NotePermission]

    def get_queryset(self):
        queryset = Event.objects.filter(entry=self.kwargs['entry_pk'])

        if self.request.method == 'GET':
            return queryset.order_by('-created_at')

        return queryset

    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(entry_id=self.kwargs['entry_pk'])
