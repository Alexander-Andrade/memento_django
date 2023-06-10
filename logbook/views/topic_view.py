from rest_framework import viewsets, permissions, mixins
from rest_framework.authentication import TokenAuthentication
from ..serializers import TopicSerializer
from ..models import Topic


class TopicView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = TopicSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Topic.objects.filter(user=self.request.user)
