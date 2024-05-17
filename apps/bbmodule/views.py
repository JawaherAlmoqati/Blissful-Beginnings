from django.shortcuts import render
from .models import bbWeb

def index(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/index.html')


def MakeUpList(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/MakeUpList.html')


def HairList(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/HairList.html')


def PhotoList(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/PhotoList.html')


def Bridemaid(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/Bridemaid.html')


def Home(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/Home.html')


def search(request):
    if request.method == "POST":
       keyword = request.POST['keyword']
       return render(request, 'bbmodule/search.html', {'keyword':keyword})
    else:
       return render(request, 'bbmodule/search.html')
    




