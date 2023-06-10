from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from ..serializers import NoteSerializer
from ..models import Entry
from ..permissions import NotePermission


class NoteNestedView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, NotePermission]

    def get_queryset(self):
        queryset = Entry.objects.filter(topic=self.kwargs['entry_pk'])

        if self.request.method == 'GET':
            return queryset.order_by('-created_at')

        return queryset

    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(entry_id=self.kwargs['entry_pk'])
