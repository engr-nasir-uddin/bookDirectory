from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Booklist
from django.db.models import Q

# Create your views here.

def index(request):
    if 'query' in request.GET:
        query=request.GET['query']
        # books=Booklist.objects.filter(title__icontains=query)
        multiple_query=Q(Q(title__icontains=query) | Q(author__icontains=query) | Q(price__icontains=query))
        books=Booklist.objects.filter(multiple_query)
    else:   
        books=Booklist.objects.all()
    return render(request, 'index.html', {'books': books})

def add(request):
    return render(request,'add.html')

def insert(request):
    title=request.POST['title']
    author=request.POST['author']
    price=request.POST['price']

    book=Booklist(title=title, author=author, price=price)
    book.save()

    return redirect('/')

def edit(request, id):
    book=Booklist.objects.get(pk=id)
    context={
        'book': book,
    }
    return render(request, 'edit.html', context)

def update(request, id):
    book=Booklist.objects.get(pk=id)
    book.title=request.GET['title']
    book.author=request.GET['author']
    book.price=request.GET['price']

    book.save()
    return redirect('/')

def delete(request, id):
    book=Booklist.objects.get(pk=id)
    book.delete()
    return redirect('/')
