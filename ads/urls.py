from django.urls import path
from ads.views import ListAdsView, AdsAPI

urlpatterns = [
    path('list', ListAdsView.as_view(), name='ads-all'),
    path('status', AdsAPI.as_view(), name='update-status')
]