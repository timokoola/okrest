from rest_framework import serializers
from api.models import Heading
from django.contrib.auth.models import User


class HeadingSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Heading
        fields = ('id', 'original', 'owner', 'url', 'corrected',
                  'notes', 'contributor', 'timestamp')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
