from django.shortcuts import render
from django.views.generic.base import View, HttpResponse

class Index(View):
    def get(self, request):
        return HttpResponse('GET request in INDEX PAGE')

    def post(self, request):
        return HttpResponse('POST request in INDEX PAGE')
