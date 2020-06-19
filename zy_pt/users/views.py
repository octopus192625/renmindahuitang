from django.shortcuts import render
from django import http
from django.views import View
import json
# Create your views here.

class Cs_views(View):

    def get(self, request):
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name)
        print(age)

        response = http.HttpResponse('咬我呀')
        response.set_cookie('name', name, max_age=3600)
        value = request.COOKIES.get('name')
        print(value)

        return response

    def post(self, request):
        json_str = request.body.decode()
        json_dict = json.loads(json_str)
        username = json_dict.get('username')
        password = json_dict.get('password')
        print(username)
        print(password)

        request.session['username'] = username
        value = request.session.get('username')
        print(value)

        return http.JsonResponse({'Q':'W'})


