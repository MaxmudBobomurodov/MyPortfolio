from django.shortcuts import render

def view_post(request):
    return render(request, 'home-one.html')