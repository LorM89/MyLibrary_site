from django.contrib import admin
from .models import Language, Book, Author, Genre, BookInstance


class BooksInstanceInline(admin.TabularInline):
    '''TabularInlines allow relevant information from independent models to be displayed in the same page'''
    model = BookInstance
    extra = 1


class BookInline(admin.TabularInline):
    '''these are useful to display author/book and book/bookInstance relations together'''
    model = Book
    extra = 0


@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
    '''One way of registering these models is through the register decorator'''
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]


@admin.register(Author)
class authorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


class bookInstanceAdmin(admin.ModelAdmin):
    '''another way of registering these models is through the admin.site method'''
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


'''models with single fields dont require additional admin models'''
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(BookInstance, bookInstanceAdmin)
