from django.urls import path
from ads.views import ListAdsView

urlpatterns = [
    path('ads/', ListAdsView.as_view(), name='ads-all')
]