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


class PageDetailSer(serializers.ModelSerializer):
    page_video = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = page
        fields = ('pk', 'nazv', 'title', 'page_video')
