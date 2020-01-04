from django.urls import path
from .views import PortfolioDisplay

urlpatterns = [
    path('<username>/', PortfolioDisplay.as_view())
]
