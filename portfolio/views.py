from rest_framework.generics import ListAPIView
from .models import PortfolioItem
from .serializers import PortfolioSerializer


class PortfolioDisplay(ListAPIView):
    serializer_class = PortfolioSerializer
    model = PortfolioItem
    def get_queryset(self):
        username = self.kwargs['username']
        print(username)
        queryset = self.model.objects.filter(owner__id = 1)
        return queryset

