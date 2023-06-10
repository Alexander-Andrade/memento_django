from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from ..serializers import EntrySerializer
from ..models import Entry
from ..permissions import EntryPermission


class EntryNestedView(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, EntryPermission]

    def get_queryset(self):
        queryset = Entry.objects.filter(topic=self.kwargs['topic_pk'], user=self.request.user)

        if self.request.method == 'GET':
            return queryset.order_by('-created_at')

        return queryset

    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(topic_id=self.kwargs['topic_pk'], user=self.request.user)
