from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

from .forms import ReviewForm
from .models import Movie, Actor


class MoviesView(ListView):

    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MoviesDetailView(DetailView):

    """Полное описание фильма"""

    model = Movie
    slug_field = 'url'
    template_name = 'movies/movie_detail.html'


class AddReview(View):
    """Отзывы"""

    @staticmethod
    def post(request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    """Вывод информации об актёре"""
    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"
