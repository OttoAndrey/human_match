from rest_framework.viewsets import ModelViewSet

from relationship.match.models import Match
from relationship.match.serializers import MatchSerializer


class MatchViewSet(ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
