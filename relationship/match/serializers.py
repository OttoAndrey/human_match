from human.serializers import HumanSerializer
from match.models import Match
from rest_framework.serializers import ModelSerializer


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = ['first_name', 'second_name', 'age', 'gender', 'human']

    human = HumanSerializer()
