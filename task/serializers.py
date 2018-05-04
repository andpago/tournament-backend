from rest_framework import serializers

from task.models import Task, Solution


class TaskSerializer(serializers.ModelSerializer):
    tournament = serializers.SerializerMethodField()

    def get_tournament(self, obj: Task):
        return obj.round.tournament_id

    class Meta:
        model = Task
        fields = ('id', 'title', 'author', 'text', 'round', 'tournament', 'answer')


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ('id', 'author', 'text', 'correct', 'task')
