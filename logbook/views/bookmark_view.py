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
        queryset = Bookmark.objects.filter(user=self.request.user)

        if self.request.method == 'GET':
            return queryset.order_by('-created_at')

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
