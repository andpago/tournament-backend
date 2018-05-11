from rest_framework import serializers

from task.models import Task, Solution


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ('id', 'author', 'text', 'correct', 'task')


class TaskSerializer(serializers.ModelSerializer):
    tournament = serializers.SerializerMethodField()
    solutions = SolutionSerializer(many=True)

    def get_tournament(self, obj: Task):
        return obj.round.tournament_id

    class Meta:
        model = Task
        fields = ('id', 'title', 'author', 'text', 'round', 'tournament', 'answer', 'solutions')
