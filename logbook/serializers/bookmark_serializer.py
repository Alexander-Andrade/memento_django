from rest_framework import serializers
from ..models import Bookmark, Topic


class BookmarkSerializer(serializers.ModelSerializer):
    topics = serializers.PrimaryKeyRelatedField(many=True, queryset=Topic.objects.order_by('created_at'))

    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'user_id', 'created_at', 'updated_at', 'topics')
        read_only_fields = ('user_id',)
