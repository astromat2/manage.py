from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import render


class ProVersionView(APIView):
    def post(self, request):
        serializer = ValidateSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        name_card = request.data.get('name_card')
        cvc_card = request.data.get('cvc_card')
        valid_thru = request.data.get('valid_thru')
        number_card = request.data.get('number_card')
        money = request.data.get('money')

        pro = ProUser.objects.create(
            name_card=name_card,
            cvc_card=cvc_card,
            valid_thru=valid_thru,
            number_card=number_card,
            money=money,
        )

        if pro:
            request.user.is_active = True
            return Response(f'ok')

        return Response(data=ProUserSerializers(pro).data, status=status.HTTP_201_CREATED, )


class LegTrainingView(APIView):
    def get(self, request):
        if request.user.is_active:
            training = LegExercises.objects.all()
            serializer = LegExercisesSerializers(training, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(f'not pro fersion')


class BackTrainingView(APIView):
    def get(self, request):
        if request.user.is_active:
            training = BackExercises.objects.all()
            serializer = BackExercisesSerializers(training, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response('not pro fersion')