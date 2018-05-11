from rest_framework import serializers

from round.models import Tournament, Round
from task.serializers import TaskSerializer


class RoundSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    tasks = TaskSerializer(many=True)

    def get_author(self, obj: Round):
        return obj.tournament.author_id

    class Meta:
        model = Round
        fields = ('id', 'title', 'tournament', 'author', 'is_final', 'is_selection', 'tasks')


class TournamentSerializer(serializers.ModelSerializer):
    rounds = RoundSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ('id', 'title', 'author', 'rounds', 'description')
