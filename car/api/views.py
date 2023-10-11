from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from car.api.serializers import CarSerializer
from car.models import Car


class CarViewSet(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer