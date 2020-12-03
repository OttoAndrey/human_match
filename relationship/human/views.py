from rest_framework.viewsets import ModelViewSet

from relationship.human.models import Human
from relationship.human.serializers import HumanSerializer


class HumanViewSet(ModelViewSet):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
