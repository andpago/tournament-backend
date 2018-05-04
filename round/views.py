from rest_framework import viewsets

from round.models import Tournament, Round
from round.serializers import TournamentSerializer, RoundSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.filter(is_deleted=False)


class RoundViewSet(viewsets.ModelViewSet):
    serializer_class = RoundSerializer
    queryset = Round.objects.filter(is_deleted=False)
