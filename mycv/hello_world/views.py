from django.shortcuts import render

# Create your views here.
def cv(request):
    return render(request, "index.html", {})

def cv1(request):
    return render(request, "cv1.html", {})
