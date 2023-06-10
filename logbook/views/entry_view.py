from rest_framework import viewsets, permissions, mixins
from rest_framework.authentication import TokenAuthentication
from ..serializers import EntrySerializer
from ..models import Entry


class EntryView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = EntrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)
