from django.urls import path


from social_network.views import (PostListCreateAPIView,
                                  PostRetrieveUpdateDestroyAPIView,
                                  LikeCreateDestroyAPIView)


app_name = 'social_network'


urlpatterns = [
    path('posts', PostListCreateAPIView.as_view(), name='api-post-list-create'),
    path('posts/<slug>', PostRetrieveUpdateDestroyAPIView.as_view(),
         name='api-retrieve-update-destroy-post'),
    path('posts/<slug>/like', LikeCreateDestroyAPIView.as_view(),
         name='api-create-destroy-like'),
]
