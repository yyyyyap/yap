from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render, redirect
from .models import Book,Reviews
from django.core.paginator import Paginator
from .forms import ReviewForm
def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        books_list = Book.objects.filter(title__contains=searchTerm)
    else:
        books_list = Book.objects.all()
    paginator = Paginator(books_list, 2)
    page_number = request.GET.get('page', 1)
    books = paginator.page(page_number)
    return render(request, 'bookhome.html', {'searchTerm':searchTerm, 'books':books})

def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Reviews.objects.filter(book=book)
    return render(request, 'bookdetail.html', {'book': book})

def createbookreview(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'GET' :
        return render(request, 'createbookreview.html' ,
        {'form':ReviewForm , 'book':book})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.book = book
            newReview.save()
            return redirect('bookdetail',newReview.book.id)
        except ValueError:
            return render(request,'createbookreview.html', {'form':ReviewForm, 'error':'非法数据'})