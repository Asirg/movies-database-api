from django.http import HttpResponse

from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return HttpResponse(movies)