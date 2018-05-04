from rest_framework import serializers

from round.models import Tournament, Round


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ('title', 'author')


class RoundSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj: Round):
        return obj.tournament.author_id

    class Meta:
        model = Round
        fields = ('title', 'tournament', 'author')
