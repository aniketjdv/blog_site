from rest_framework import serializers
from api.models import BlogModel


class BlogSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=BlogModel
        fields='__all__'

    # user = serializers.HyperlinkedRelatedField(
    #     view_name='username',  # This must match the view name in your URLs
    #     queryset=User.objects.all()
    # )