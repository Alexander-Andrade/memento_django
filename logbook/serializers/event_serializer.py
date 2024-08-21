from rest_framework import serializers
from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'description', 'files', 'entry_id', 'minimized', 'starts_at', 'created_at', 'updated_at')
