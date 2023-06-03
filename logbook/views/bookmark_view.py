from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from ..serializers import BookmarkSerializer
from ..models import Bookmark
import pdb


class BookmarkView(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
