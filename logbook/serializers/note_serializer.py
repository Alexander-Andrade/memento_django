from rest_framework import serializers
from ..models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'description', 'files', 'entry_id', 'minimized', 'created_at', 'updated_at')
