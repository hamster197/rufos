from collections import OrderedDict

from rest_framework import serializers

from fl.models import page, content




class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = content
        fields = ('pk', 'tip_contenta', 'title', 'counter', 'video_url', 'video_sub_url', 'audio_url', 'text')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret

class PageIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = page
        fields = ('pk', 'nazv', 'title','url')

class PageDetailSerializer(serializers.ModelSerializer):
    pages = ContentSerializer(many=True, read_only=True)
    class Meta:
        model = page
        fields = ('pk', 'nazv', 'title', 'pages',)