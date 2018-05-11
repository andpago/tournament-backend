from django import http
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request

from task.models import Task, Solution
from task.serializers import TaskSerializer, SolutionSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(is_deleted=False)
    serializer_class = TaskSerializer

    def retrieve(self, request, pk):
        print(request.user)

        if request.user.is_anonymous:
            return http.HttpResponseForbidden()

        try:
            task = Task.objects.get(id=pk)
        except Task.DoesNotExist:
            return http.HttpResponseNotFound()

        data = TaskSerializer(task).data
        data['solutions'] = [sol for sol in data['solutions'] if sol['author'] == request.user.id]

        return http.JsonResponse(data)


class SolutionViewSet(viewsets.ModelViewSet):
    serializer_class = SolutionSerializer

    def get_queryset(self, request):
        if request.user.is_anonymous:
            return QuerySet()

        return Solution.objects.filter(author=request.user)

    @action(detail=False, methods=["PUT"])
    def submit(self, request: Request):
        REQUIRED_FIELDS = ('text', 'task')

        if request.user.is_anonymous:
            return http.HttpResponseForbidden()

        for field in REQUIRED_FIELDS:
            if field not in request.POST:
                return http.HttpResponseBadRequest()

        try:
            task = Task.objects.get(id=request.POST['task'])
        except Task.DoesNotExist:
            return http.HttpResponseBadRequest()

        solution = Solution(author=request.user,
                            task=task,
                            text=request.POST['text'])

        solution.save()

        return http.JsonResponse({'status': 'ok'})
