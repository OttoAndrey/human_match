from match.models import Match
from match.serializers import MatchSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class MatchViewSet(ReadOnlyModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
