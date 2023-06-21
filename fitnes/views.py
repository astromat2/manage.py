from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import datetime


class EyeTrainingView(APIView):
    def get(self, request):
        """
        Получите список упражнений для глаз.

        Возвращает:
        - данные: сериализованный список упражнений для глаз.
        - статус: код состояния HTTP 200 (ОК).
        """
        training = EyeExercises.objects.all()
        serializer = EyeExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class HandTrainingView(APIView):
    def get(self, request):
        """
        Получить список упражнений для рук.

        Возвращает:
        - данные: сериализованный список упражнений для рук.
        - статус: код состояния HTTP 200 (ОК).
        """
        training = HandExercises.objects.all()
        serializer = HandExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class NeckTrainingView(APIView):
    def get(self, request):
        """
        Найдите список упражнений для шеи.

        Возвращает:
        - данные: сериализованный список упражнений для шеи.
        - статус: код состояния HTTP 200 (ОК).
        """
        training = NeckExercises.objects.all()
        serializer = NeckExercisesSerializers(training, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class StartStopView(APIView):
    def get(self, request):
        """
        Получите результат разницы во времени между запуском и остановкой.
        Возвращает:

        - сколько минут занимался человек
        - данные: строковое представление разницы во времени.
        - статус: код состояния HTTP 200 (ОК).
        """
        start = datetime.   datetime.now()
        stop = datetime.datetime.now()
        result = start - stop
        day = []
        day.append(result)
        return Response(data=f'результат {result}', status=status.HTTP_200_OK)