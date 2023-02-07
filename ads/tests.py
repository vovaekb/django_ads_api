from .models import Ad
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import json

TEST_SIZE = 10


class TestAds(APITestCase):
    def setUp(self):
        self.ids = list(range(5))
        self.payd_data = {'status': 'оплачено', 'ids': self.ids}
        self.ads = []
        for i in range(TEST_SIZE):
            self.ads.append(Ad.objects.create(title='Test ad {}'.format(i), category='разное', status='отказ')) 

    def test_update_ads(self):
        # Correct case
        response = self.client.put(
            reverse('ads/status'),
            data=json.dumps(self.payd_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)