from rest_framework.viewsets import ModelViewSet

from match.models import Match
from match.serializers import MatchSerializer


class MatchViewSet(ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
