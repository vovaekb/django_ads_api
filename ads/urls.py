from django.urls import path
from ads.views import ListAdsView

urlpatterns = [
    path('list', ListAdsView.as_view(), name='ads-all')
]