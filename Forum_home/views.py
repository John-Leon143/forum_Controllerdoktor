from django.shortcuts import render

# Create your views here.

def forum_home(request):


    return render(request, 'Forum_home/forum_home.html')
