from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from ..serializers import TopicSerializer
from ..models import Topic
from ..permissions import TopicPermission


class TopicNestedView(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, TopicPermission]

    def get_queryset(self):
        queryset = Topic.objects.filter(bookmark=self.kwargs['bookmark_pk'], user=self.request.user)

        if self.request.method == 'GET':
            return queryset.order_by('-created_at')

        return queryset

    def create(self, request, *args, **kwargs):
        self.check_object_permissions(request, None)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(bookmark_id=self.kwargs['bookmark_pk'], user=self.request.user)
