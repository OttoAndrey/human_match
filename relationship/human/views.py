from human.models import Human
from human.serializers import HumanSerializer
from rest_framework.viewsets import ModelViewSet


class HumanViewSet(ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
