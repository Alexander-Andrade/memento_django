from rest_framework import serializers
from ..models import Bookmark, Topic


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'user_id', 'created_at', 'updated_at')
        read_only_fields = ('user_id',)
