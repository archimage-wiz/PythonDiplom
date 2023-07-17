from celery.result import AsyncResult
from django.http import JsonResponse
from rest_framework.views import APIView

from orders.celery import celery_app


class ViewTask(APIView):

    def get(self, request, *args, **kwargs):
        if task_id := request.query_params.get('task_id'):
            task = AsyncResult(task_id, app=celery_app)
            return JsonResponse({"Status": task.status,
                                 "result": task.result})
        return JsonResponse({"Status": "Error",
                             "Details": "provide task_id"},
                            json_dumps_params={'ensure_ascii': False})
