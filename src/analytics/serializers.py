from rest_framework import serializers

from account.models import Account


class LikeAnlyticsSerializer(serializers.Serializer):
    date = serializers.DateField()
    likes_count = serializers.IntegerField()


class UserAnayticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username', 'last_login', 'last_request']
