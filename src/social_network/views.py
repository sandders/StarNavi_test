from django.db import IntegrityError

from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView)
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from social_network.models import Post, Like
from social_network.paginators import PostPaginator
from social_network.serializers import PostSerializer, LikeSerializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPaginator
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        try:
            serializer.save(author=self.request.user)
        except IntegrityError:
            raise ValidationError(
                {'detail': 'You allready have post with that name'})


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise ValidationError(
                {'detail': 'You are not an author of this post'})
        serializer.save()

    def perform_destroy(self, post):
        if self.request.user != post.author:
            raise ValidationError(
                {'detail': 'You are not an author of this post'})
        post.delete()

    def partial_update(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(slug=kwargs['slug'])
        except Post.DoesNotExist:
            raise NotFound('Post not found')
        if request.user != post.author:
            raise ValidationError(
                {'detail': 'You are not an author of this post'})
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class LikeCreateDestroyAPIView(CreateModelMixin,
                               DestroyModelMixin,
                               GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes([IsAuthenticated])

    def get_object(self):
        owner = self.request.user
        liked_post_slug = self.kwargs['slug']
        try:
            like = Like.objects.get(
                owner=owner, liked_post__slug=liked_post_slug)
        except:
            raise ValidationError(
                {'detail': "You haven't liked liked this post"})
        return like

    def perform_create(self, serializer):
        try:
            post = Post.objects.get(slug=self.kwargs['slug'])
        except Post.DoesNotExist:
            raise NotFound('Post not found')

        try:
            serializer.save(owner=self.request.user, liked_post=post)
        except IntegrityError:
            raise ValidationError(
                {'detail': "You've allready liked this post"})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        a = self.destroy(request, *args, **kwargs)
        return a
