from django.shortcuts import render,redirect
from django.views import View
from .models import UserProfileInfo
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class UserRegistration(View):
    template_name ="authsignup.html"
    def get(self,request,*args, **kwargs):
        content = {}
        form = UserForm
        registered = False
        if request.user.is_authenticated:
            return redirect("authbasic:index")
        else:
            content['form'] = form
            content['registered'] = registered
        return render(request,self.template_name,content)
    def post(self,request,*args, **kwargs):
        content = {}
        form = UserForm(request.POST)
        registered = False
        if request.user.is_authenticated:
            return redirect("authbasic:index")
        else:
            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                registered = True
            else:
                # print errors // this is debug area
                pass
            content['form'] = form
            content['registered'] = registered
        return render(request,self.template_name,content)

class UserSignin(View):
    template_name = "authlogin.html"
    def get(self,request,*args, **kwargs):
        content = {}
        if request.user.is_authenticated:
            return redirect("authbasic:index")
        else:
            pass
        return render(request,self.template_name,content)
    def post(self,request,*args, **kwargs):
        content = {}
        if request.user.is_authenticated:
            return redirect("authbasic:index")
        else:
                uname = request.POST.get('username')
                passw = request.POST.get('password')
                user = authenticate(
                    request,
                    username=uname,password=passw,      
                )
                if user is not None and user.is_active:
                    login(request,user)
                    return redirect("authbasic:index")
                else:
                    return redirect("authbasic:signup")
                
        return render(request,self.template_name,content)

@login_required
def user_logout(request):
    logout(request)
    return redirect("authbasic:signin")

def index(request):
    # print(request.user.is_authenticated) #debug
    return render(request,'authbasic.html')