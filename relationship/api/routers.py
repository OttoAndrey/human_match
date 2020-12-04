from rest_framework import routers

from human.views import HumanViewSet
from match.views import MatchViewSet

router = routers.DefaultRouter()
router.register('human', HumanViewSet, basename='human')
router.register('match', MatchViewSet, basename='match')
