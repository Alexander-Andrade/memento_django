from rest_framework import serializers
from ..models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'bookmark_id', 'user_id', 'created_at', 'updated_at')
        read_only_fields = ('user_id',)
