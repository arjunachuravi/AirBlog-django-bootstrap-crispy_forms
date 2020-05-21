from django.shortcuts import get_object_or_404, redirect, render
from .models import relativity
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import relativity
from .forms import TheEditor,TheEditorUpdater
from django.contrib import messages

class PostObjectMixin(object):
    model = relativity
    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model,pk=pk)
        return obj

class CreateThePost(LoginRequiredMixin,View):
    template_name="relations/createpost.html"
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
    template_name="relations/ReadPost.html"
    login_url = "authbasic:signin"
    def get(self,request,*args, **kwargs):
        content = {
            "objects" : relativity.objects.all()
        }
        return render(request,self.template_name,content)

class UpdateThePost(PostObjectMixin,LoginRequiredMixin,View):
    template_name = "relations/updatepost.html"
    login_url = 'authbasic:signin'
    def get(self,request,id=None,*args, **kwargs):
        content = {}
        obj = self.get_object()
        if obj is not None:
            form = TheEditorUpdater(instance=obj)
            content['object'] = obj
            content['form'] = form
        return render(request,self.template_name,content)
    def post(self,request,id=None,*args, **kwargs):
        content = {}
        obj = self.get_object()
        if obj is not None:
            form = TheEditorUpdater(request.POST,instance=obj)
            if form.instance.author == request.user:
                if form.is_valid():
                    form.save()
                    messages.success(request,"You have edited the Post")
                    return redirect("relations:read")
            else:
                    messages.error(request,"you cant change other member's post")
            content['object'] = obj
            content['form'] = form
        return render(request,self.template_name,content)

class DeleteThePost(PostObjectMixin,LoginRequiredMixin,View):
    template_name = "relations/deletepost.html"
    def get(self,request,id=None,*args, **kwargs):
        content = {}
        obj = self.get_object()
        if obj is not None:
            content['obj'] = obj
        return render(request,self.template_name,content)
    
    def post(self,request,id=None,*args, **kwargs):
        content = {}
        obj = self.get_object()
        if obj.author == request.user:
            if obj is not None:
                obj.delete()
                content['obj'] = None
                messages.info(request,"The post was Deleted")
                return redirect('relations:read') 
        else:
            messages.info(request, 'You cannot delete others tweet')
        return render(request,self.template_name,content)

class RetriveThePost(PostObjectMixin,LoginRequiredMixin,View):
    template_name="relations/retrivepost.html"
    login_url = "authbasic:signin"
    def get(self,request,id=None,*args, **kwargs):
        content = {}
        obj = self.get_object()
        if obj is not None:
            form = TheEditorUpdater(instance=obj)
            content['obj'] = obj
        return render(request,self.template_name,content)