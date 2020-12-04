from rest_framework.serializers import ModelSerializer

from human.models import Human


class HumanSerializer(ModelSerializer):
    class Meta:
        model = Human
        fields = ['avatar', 'first_name', 'second_name', 'age', 'gender']
