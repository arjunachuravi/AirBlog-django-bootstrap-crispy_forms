from django.shortcuts import redirect, render
from .models import relativity
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import relativity
from .forms import TheEditor

class CreateThePost(LoginRequiredMixin,View):
    template_name="createpost.html"
    login_url = "authbasic:signin"
    def get(self,request,*args, **kwargs):
        content = {}
        form = TheEditor()
        content['form'] = form
        return render(request,self.template_name,content)
    def post(self,request,*args, **kwargs):
        content = {}
        form = TheEditor(request.POST)
        if form.is_valid:
            form.save(commit=False)
            form.instance.author = request.user
            form.save()
            return redirect("relations:read")
        content = {
            "form" : form
        }
        return render(request,self.template_name,content)

class ReadThePost(LoginRequiredMixin,View):
    template_name="ReadPost.html"
    login_url = "authbasic:signin"
    def get(self,request,*args, **kwargs):
        content = {
            "objects" : relativity.objects.all()
        }
        return render(request,self.template_name,content)