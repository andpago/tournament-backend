from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    tournament = serializers.SerializerMethodField()

    def get_tournament(self, obj: Task):
        return obj.round.tournament_id

    class Meta:
        model = Task
        fields = ('title', 'author', 'text', 'round', 'tournament', 'answer')
