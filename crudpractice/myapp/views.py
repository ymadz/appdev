from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book

def home(request):
    return render(request, 'home.html')

# ======= Author Views =======
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'items': authors})

def author_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Author.objects.create(name=name)
    return redirect('author_list')

def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.name = request.POST['name']
        author.save()
        return redirect('author_list')
    return render(request, 'author_edit.html', {'item': author})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('author_list')

# ======= Book Views =======
def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'book_list.html', {'items': books, 'authors': authors})

def book_save(request):
    if request.method == 'POST':
        title = request.POST['name']
        description = request.POST['description']
        author_id = request.POST['author_id']
        author = get_object_or_404(Author, pk=author_id)
        Book.objects.create(title=title, author=author)
    return redirect('book_list')

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = Author.objects.all()
    if request.method == 'POST':
        book.title = request.POST['name']
        book.author_id = request.POST['author_id']
        book.save()
        return redirect('book_list')
    return render(request, 'book_edit.html', {'item': book, 'authors': authors})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
