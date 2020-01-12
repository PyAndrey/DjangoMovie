from datetime import date

from django.db import models


class Category(models.Model):

    """Категории"""

    name = models.CharField("Название", max_length=150)
    descriptions = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Actor(models.Model):

    """Актёры и режиссеры"""

    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    descriptions = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/", height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = "Актёры и режиссеры"
        verbose_name_plural = "Актёры и режиссеры"

    def __str__(self):
        return self.name


class Genre(models.Model):

    """Жанры"""

    name = models.CharField("Имя", max_length=100)
    descriptions = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name

class Movie(models.Model):

    """Фильмы"""

    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    descriptions = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/", height_field=None, width_field=None, max_length=None)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premier = models.DateField("Премьера в мире", auto_now=False, auto_now_add=False, default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="указать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="указать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title


class MoviesShots(models.Model):

    """Кадры из фильма"""

    title = models.CharField("Заголовок", max_length=100)
    descriptions = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/", height_field=None, width_field=None, max_length=None)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"

    def __str__(self):
        return self.title


class RatingStar(models.Model):

    """Звезда рейтинга"""

    value = models.SmallIntegerField("Значение", default=0)


    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"

    def __str__(self):
        return self.value


class Rating(models.Model):

    """Рейтинг"""

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name="звезда", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Reviews(models.Model):

    """Отзывы"""

    email = models.EmailField("Эмейл", max_length=254)
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Родитель", on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.name} - {self.movie}"

