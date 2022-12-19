from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name','' )
        descri = request.POST.get('descri','' )
        year = request.POST.get('year','' )
        img = request.FILES['img']
        movies = Movie(name=name, descri=descri, year=year, img=img)
        movies.save()

    return render(request, 'add.html')


def update(request, id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        forms = MovieForm(request.POST or None, request.FILES, instance=movie)
        if forms.is_valid():
            return redirect('/')
    return render(request, 'edit.html', {'form': forms, 'movie': movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')