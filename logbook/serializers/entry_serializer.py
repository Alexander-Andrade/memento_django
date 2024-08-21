from rest_framework import serializers
from ..models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'title', 'description', 'files', 'topic_id', 'minimized', 'created_at', 'updated_at', 'user_id')
        read_only_fields = ('user_id',)
