from collections import OrderedDict
from datetime import datetime, date

from django.db.models import Count
from django.db.models.functions import TruncDay, Cast

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from analytics.serializers import LikeAnlyticsSerializer
from social_network.models import Like


@api_view(['GET', ])
@permission_classes([IsAdminUser])
def like_analytics_view(request):
    date_from = request.query_params.get('date_from', '')

    try:
        date_from_obj = datetime.strptime(date_from, r'%Y-%m-%d')
    except ValueError:
        return Response({'date_from': 'Invalid date format, use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

    date_to = request.query_params.get(
        'date_to', datetime.strftime(date.today(), r'%Y-%m-%d'))

    try:
        date_to_obj = datetime.strptime(date_to, r'%Y-%m-%d')
    except ValueError:
        return Response({'date_to': 'Invalid date format, use YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)

    if date_from_obj > date_to_obj:
        return Response({'detail': 'date_from can not be greater than date_to'}, status=status.HTTP_400_BAD_REQUEST)

    likes_for_period = Like.objects.filter(
        date_liked__range=[date_from, date_to])

    if not likes_for_period.exists():
        return Response({'detail': 'No data for this period'})

    likes_for_period_aggregated = likes_for_period.annotate(date=TruncDay(
        'date_liked')).values('date').annotate(likes_count=Count('id')).values('date', 'likes_count')

    serializer = LikeAnlyticsSerializer(
        data=list(likes_for_period_aggregated), many=True)
    if serializer.is_valid():
        new_data = {
            'likes_by_date': serializer.data,
            'total_likes_for_period': likes_for_period.count()
        }
        return Response(data=new_data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
