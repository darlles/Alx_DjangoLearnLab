# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id', 'recipient', 'actor', 'actor_username', 'verb',
            'target_content_type', 'target_object_id', 'target_repr',
            'timestamp', 'is_read'
        ]
        read_only_fields = ['id', 'recipient', 'actor', 'actor_username', 'timestamp']

    def get_target_repr(self, obj):
        return str(obj.target) if obj.target else None