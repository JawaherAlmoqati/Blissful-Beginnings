from django.shortcuts import render

def index(request):
    # 1-study the request
    # 2-back to template
    return render(request, 'bbmodule/index.html')

