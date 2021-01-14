from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """View function for home page of site: generates counts of
        important objects and filters for status and title"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    filtered_books = Book.objects.filter(title__icontains='The').count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # The variable that is passed to the index.html template
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'filtered_books': filtered_books,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains='A')[:5]


class BookDetailView(generic.DetailView):
    model = Book
