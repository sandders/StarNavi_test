from rest_framework import serializers
from social_network.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_post_author')

    class Meta:
        model = Post
        fields = ['title', 'date_published',
                  'date_updated', 'content', 'author']
        read_only_fields = ['author']

    def get_post_author(self, post):
        return post.author.username


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ()
