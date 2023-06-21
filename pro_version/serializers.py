from rest_framework import serializers
from pro_version.models import *


class ProUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = '__all__'


class LegExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LegExercises
        fields = '__all__'


class BackExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model = BackExercises
        fields = '__all__'


class ValidateSerializers(serializers.Serializer):
    number_card = serializers.IntegerField()
    cvc_card = serializers.IntegerField()
    valid_thru = serializers.IntegerField()
    name_card = serializers.CharField()
    money = serializers.IntegerField()