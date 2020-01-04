from rest_framework import serializers
from .models import PortfolioItem


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = ('title', 'body', 'img', 'owner')
