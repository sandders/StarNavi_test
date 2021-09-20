from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from social_network.models import Post
from social_network.paginators import PostPaginator
from social_network.serializers import PostSerializer

from account.models import Account


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPaginator
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise ValidationError(
                {'response': 'You are not an author of this post'})
        serializer.save()

    def perform_destroy(self, post):
        if self.request.user != post.author:
            raise ValidationError(
                {'response': 'You are not an author of this post'})

    def partial_update(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs['slug'])
        if request.user != post.author:
            raise ValidationError(
                {'response': 'You are not an author of this post'})
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
