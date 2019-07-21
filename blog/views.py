from django.shortcuts import render

def home(request):
    print(request)
    template_name= "index.html"
    return render(request,template_name)      