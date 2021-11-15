from rest_framework import serializers
from conveyor.models import *


class PostsStateSerializer(serializers.ModelSerializer):
    post_number = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = PostsState
        fields = ['status_post', 'post_number']


class ButtonsBlocksSerializer(serializers.ModelSerializer):
    posts_state = PostsStateSerializer(many=False)

    class Meta:
        model = ButtonsBlocks
        fields = ('buttons_block_number', 'posts_state')
