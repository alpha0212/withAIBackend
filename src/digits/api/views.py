from rest_framework import viewsets
from ..models import Digit
from .serializers import DigitSerializer
from rest_framework.permissions import IsAuthenticated


class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitSerializer
    permisson_classes = (IsAuthenticated,)
    queryset = Digit.objects.all()
