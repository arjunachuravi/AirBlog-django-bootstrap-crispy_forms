from django.shortcuts import render,get_object_or_404
from .models import myprojectblog
from django.views import View

from django.views.generic.list import ListView

class GreetingView(View):
    greeting = ""

    def get(self, request):
        return render(request, 'greet.html', {"greeting":self.greeting})

# class blogpostListView(View):
#     template_name="post_list.html"
#     queryset = blogpost.objects.all()
#     def get_queryset(self):
#         return self.queryset
#     def get(self,request,*args, **kwargs):
#         content = {
#             "obj_list":self.get_queryset()
#         }
#         return render(request,self.template_name,content)

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
