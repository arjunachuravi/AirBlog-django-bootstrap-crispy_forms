from django.shortcuts import render
from .models import myprojectblog
from django.views import View

from django.views.generic.list import ListView

class GreetingView(View):
    greeting = ""

    def get(self, request):
        return render(request, 'greet.html', {"greeting":self.greeting})

class postlistView(View):

    def get(self,request):
        return render(request,"postlist.html",{"objects":myprojectblog.objects.all()})