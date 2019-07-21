from django.shortcuts import render
from django.views import View
from account.forms import UserSignUpForm


class UserSignUpView(View):
    def get(self,request):
        template_name = "account/signup.html"
        form= UserSignUpForm()
        print(request)
        return render(request,template_name,{'form':form})

    def post(self,request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            print(form.cleaned_data)
            raw_password =form.cleaned_data['password1']
            username =form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()
            return render(request,"account/success.html")
        return render(request,"account/signup.html" ,{'form':form}) 