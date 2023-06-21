from rest_framework import viewsets
from .models import YourModel
from .serializers import YourModelSerializer
from .filters import YourModelFilter


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    filterset_class = YourModelFilter