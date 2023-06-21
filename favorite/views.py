from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework import status




class FavoriteExerciseListCreateAPIView(ListCreateAPIView):
    serializer = ExerciseSerializer

    def get_queryset(self):
        user = self.request.user
        return user.favorite_exercises.all()

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

    def delete(self, request, *args, **kwargs):
        exercise_id = kwargs.get('id')
        user = request.user
        exercise = Exercise.objects.filter(id=exercise_id, users=user).first()
        if exercise:
            exercise.users.remove(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
