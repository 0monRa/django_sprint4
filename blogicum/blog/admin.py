from django.contrib import admin

from .models import Category, Location, Post

empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Поля списка объектов
    list_display = (
        'title',
        'is_published',
        'author',
        'text',
        'category',
    )
    # Поля для редактирования
    list_editable = (
        'category',
        'is_published',
        'text',
    )
    # Поиск по полям см. ниже
    search_fields = ('title', 'author',)
    # Фильтрация по полям см. ниже
    list_filter = ('category',)
    list_display_links = ('title',)


class PostInLine(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )


admin.site.register(Location)
