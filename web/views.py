from rest_framework import status
from django.views import View
from django.http import HttpResponse

class TestView(View):
    def get(self, request):
        return HttpResponse("This is a test view.", status=status.HTTP_200_OK)
