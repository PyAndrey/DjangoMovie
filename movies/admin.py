from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Actor, Category, Genre, Movie, MovieShots, Rating,
                     RatingStar, Reviews)


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display: tuple = ("id", "name", "url")
    list_display_links: tuple = ("name",)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra: int = 1
    readonly_fields: tuple = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110">')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "category", "url", "draft")
    list_filter: tuple = ("category", "year")
    search_fields: tuple = ("title", "category__name")
    readonly_fields = ("get_image", )
    inlines: list = [MovieShotsInline, ReviewInline]
    save_on_top: bool = True
    save_as: bool = True
    actions = ['published', 'unpublished']
    list_editable: tuple = ("draft",)
    form = MovieAdminForm
    fieldsets: tuple = (
        (None, {
            'fields': (("title", "tagline"), )
        }),
        (None, {
            'fields': ("description", ("poster", "get_image"))
        }),
        (None, {
            'fields': (("year", "world_premier", "country"),)
        }),
        ("Actors", {
            'classes': ("collapse",),
            'fields': (("actors", "directors", "genres", "category"), )
        }),
        (None, {
            'fields': (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            'fields': (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60">')

    def unpublished(self, request, queryset):
        """Снять с публикации"""
        row_update: int = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, message_bit)

    def published(self, request, queryset):
        """Опубликовать"""
        row_update: int = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, message_bit)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ('change',)

    published.short_description = "Опубликовать"
    published.allowed_permissions = ('change',)

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display: tuple = ("name", "email", "parent", "movie", "id")
    readonly_fields: tuple = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display: tuple = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display: tuple = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display: tuple = ("movie", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display: tuple = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"