from django.shortcuts import render
from .models import myprojectblog
from django.views import View

class GreetingView(View):
    greeting = ""

    def get(self, request):
        return render(request, 'greet.html', {"greeting":self.greeting})
