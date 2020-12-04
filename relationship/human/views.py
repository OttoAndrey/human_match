from rest_framework.viewsets import ModelViewSet

from human.models import Human
from human.serializers import HumanSerializer


class HumanViewSet(ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
