from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from human.models import Human
from match.models import Match
from match.serializers import MatchSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


def match_human(request, human_id):
    human = get_object_or_404(Human.objects.prefetch_related('matches'), pk=human_id)

    for match in human.matches.all():
        data = {
            'first_name': match.first_name,
            'second_name': match.second_name,
            'age': match.age,
            'gender': match.gender,
            'human': {
                'avatar': human.avatar.url,
                'first_name': human.first_name,
                'second_name': human.second_name,
                'age': human.age,
                'gender': human.gender,
            }
        }

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})


class MatchViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
