from django.contrib import admin

from .models import (Actor, Category, Genre, Movie, MoviesShots, Rating,
                     RatingStar, Reviews)

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MoviesShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
