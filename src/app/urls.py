from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls'), name='api-account'),
    path('api/analytics/', include('analytics.urls'), name='api-analytics'),
    path('api/posts/', include('social_network.urls'), name='api-posts'),
]
