from rest_framework import routers

from relationship.human.views import HumanViewSet
from relationship.match.views import MatchViewSet

router = routers.DefaultRouter()
router.register('human', HumanViewSet, basename='human')
router.register('users', MatchViewSet, basename='match')
