from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from django.views.generic.list import ListView

from .models import myprojectblog

from .forms import postform
class postcreateview(View):

    template_name = "createpost.html"

    def get(self,request,id=None,*args, **kwargs):
        content = {}
        form = postform()
        content['form'] = form
        return render(request,self.template_name,content)
    
    def post(self,request,id=None,*args, **kwargs):
        content = {}
        form = postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogpost:list")
        content['form'] = form
        return render(request,self.template_name,content)


class GreetingView(View):
    greeting = ""

    def get(self, request):
        return render(request, 'greet.html', {"greeting":self.greeting})

class getmyobjmixin(object):
    model = myprojectblog
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model,id=id)
        return obj

class blogpostView(getmyobjmixin,View):
    template_name = "postdetail.html"
    def get(self,request,*args, **kwargs):
        content ={
            'obj':self.get_object()
        }
        return render(request,self.template_name,content)

class postlistView(View):

    def get(self,request):
        return render(request,"postlist.html",{"objects":myprojectblog.objects.all()})

