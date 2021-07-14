from django.shortcuts import render

# Create your views here.

def gym(request):
    """ A view to return the index page """

    return render(request, 'gym/gym.html')