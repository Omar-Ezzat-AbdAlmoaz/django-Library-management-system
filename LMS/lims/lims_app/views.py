from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import BookForm,CatForm

def index(request):
    if request.method == 'POST':
        addBook = BookForm(request.POST,request.FILES)
        if addBook.is_valid():
            addBook.save()
        addCat = CatForm(request.POST)
        if addCat.is_valid():
            addCat.save()
    
    context={
        'books':Book.objects.all(),
        'categorys':Category.objects.all(),
        'form':BookForm(),
        'catform':CatForm(),
        'numberBooks':Book.objects.filter(active = True).count(),
        'bookSold':Book.objects.filter(status = 'sold').count(),
        'bookRental':Book.objects.filter(status = 'rental').count(),
        'bookAvilable':Book.objects.filter(status = 'avilable').count(),
    }
    return render(request,'pages/index.html',context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)
    
    context={
        'books':search,
        'categorys':Category.objects.all(),
        'catform':CatForm(),
    }
    return render(request,'pages/books.html',context)

def delete(request,id):
    
    book_delete =get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')

def update(request,id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context={
        'form':book_save,
    }
    return render(request,'pages/update.html',context)
