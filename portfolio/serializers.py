from rest_framework import serializers
from .models import PortfolioItem


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = ('title', 'sub_title', 'short_description', 'body', 'img', 'owner')
