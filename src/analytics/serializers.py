from rest_framework import serializers
from social_network.models import Like


class LikeAnlyticsSerializer(serializers.Serializer):
    date = serializers.DateField()
    likes_count = serializers.IntegerField()
