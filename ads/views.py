'''
Solution: https://stackoverflow.com/questions/60258388/how-to-update-multiple-objects-in-django-rest-framework
'''

from django.shortcuts import render
# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from .models import Ad
from .serializers import AdSerializer

class ListAdsView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (IsAdminUser,)


class AdsAPI(APIView):
    """
    get_object:
    get single object by ID

    validate_ids:
    check if correct IDs were privided in request payload

    put:
    update objects
    """
    permission_classes = (IsAdminUser,)
    def get_object(self, id):
        try:
            return Ad.objects.get(id=id)
        except Ad.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST
    
    def validate_ids(self, id_list):
        for id in id_list:
            try:
                Ad.objects.get(id=id)
            except (Ad.DoesNotExist):
                raise status.HTTP_400_BAD_REQUEST
        return True
    
    def put(self, request, *args, **kwargs):
        id_list = request.data['ids']
        self.validate_ids(id_list=id_list)
        if 'status' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instances = []
        for id in id_list:
            obj = self.get_object(id=id)
            obj.status = request.data['status']
            obj.save()
            instances.append(obj)
        serializer = AdSerializer(instances, many=True)
        return Response(serializer.data)
