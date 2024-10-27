from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')

def News(request):
    return render(request,'news.html')

def Mission(request):
    return render(request,'mission.html')

def Explore(request):
    return render(request,'explore.html')

def Earth(request):
    return render(request,'earth.html')