from human.models import Human
from rest_framework.serializers import ModelSerializer


class HumanSerializer(ModelSerializer):
    class Meta:
        model = Human
        fields = ['avatar', 'first_name', 'second_name', 'age', 'gender']
