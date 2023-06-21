from rest_framework import serializers


class FitnessRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    height = serializers.DecimalField(max_digits=5, decimal_places=2)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    fitness_goal = serializers.CharField(max_length=200)
    medical_conditions = serializers.CharField(max_length=200, allow_blank=True, required=False)


class YourModelSerializer(serializers.Serializer):
    pass