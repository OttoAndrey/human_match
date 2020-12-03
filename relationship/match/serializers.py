from rest_framework.serializers import ModelSerializer

from relationship.match.models import Match


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = ['first_name', 'second_name', 'age', 'gender', 'human']
