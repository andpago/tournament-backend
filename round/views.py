from rest_framework import viewsets

from round.models import Tournament, Round
from round.serializers import TournamentSerializer, RoundSerializer
from rest_framework.pagination import LimitOffsetPagination


class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.filter(is_deleted=False)
    pagination_class = LimitOffsetPagination


class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.filter(is_deleted=False)
    pagination_class = LimitOffsetPagination
