from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .forms import ReviewForm
from .models import Movie


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

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
