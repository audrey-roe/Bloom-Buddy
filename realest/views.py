from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages

from .serializers import *
from . models import realEstate_offer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from auth_api.models import user_info_extend
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.'


class realEstate_property(APIView):
    # authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serviceProvider = user_info_extend.objects.get(user_type  = "realtor")
        offer = realEstate_offer.objects.create(title = request.data['title'], location = request.data['location'], duration = request.data['duration'],
                                                description =request.data['description'], price = request.data['amount'], bedrooms = request.data['bedrooms'],
                                                toilets = request.data['toilets'],bathrooms = request.data['bathroom'],parking = request.data['parking'],
                                                state = request.data['state'], purpose = request.data['purpose'], propertyType = request.data['property_type'],
                                                youtube_link = request.data['youtube_link'],instagram_link = request.data['instagram_link'], local_government = request.data['lga'],
                                                covered_area = request.data['covered_area'], total_area = request.data['total_area'], furnished_type = request.data['furnished_type'],
                                                currency = request.data['currency'],financing = request.data['financing'], imagegallery= request.data['propertyImages'], service_provider= serviceProvider)
        if  offer:
            return Response({
            "message": "success"})
            
        else:
            return Response({"message": "failed"})
            
        

        
# corrected  this
class realEstate_OffersViews(APIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({
            "message": "success",
            "status_code" :  200}
            
        )
    
    
    
    
    
    
    
    # authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     estate = realEstate_offer.objects.all()
    #     serializer = realEstate_offerSerializer(estate, many=True)
    #     return Response({
    #         "message": "success",
    #         "data":{
    #             'data' : serializer.data
    #         },
    #         "status_code" :  200
    #             })
        # return Response({
        #                 "message": "success",
        #                 "data" : {
        #                     "location": estate.location,
        #                     "purpose": estate.purpose,
        #                     "state": estate.state,
        #                     "type": estate.propertyType,
        #                     "bedroom": estate.bathrooms,
        #                     "price": estate.price,
        #                     "duration": estate.duration,
        #                     "toilets": estate.toilets,
        #                     "bathrooms": estate.bathrooms,
        #                     "parking": estate.parking,
        #                     "imagegallery": estate.imagegallery,
        #                 },
                    
                    #     "status_code" :  200
                    # })