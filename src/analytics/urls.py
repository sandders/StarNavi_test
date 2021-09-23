from django.urls import path

from analytics.views import like_analytics_view, UserActivityAnalyticsRetrieveAPIView

urlpatterns = [
    path('likes', like_analytics_view, name='api-analytics-likes'),
    path('user_activity', UserActivityAnalyticsRetrieveAPIView.as_view(),
         name='api-analytics-user-activity')
]
