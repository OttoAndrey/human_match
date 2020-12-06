from human.views import HumanViewSet
from match.views import MatchViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('human', HumanViewSet, basename='human')
router.register('match', MatchViewSet, basename='match')
