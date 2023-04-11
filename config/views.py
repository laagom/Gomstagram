from django.shortcuts import render

from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print(f'{__class__} -> get() function!')
        return render(request, "gomstagram/main.html")

    def post(self, request):
        print(f' {__class__} -> post() function!')
        return render(request, "gomstagram/main.html")