from django.urls import path

from analytics.views import like_analytics_view

urlpatterns = [
    path('likes', like_analytics_view, name='api-analytics-likes'),
]
