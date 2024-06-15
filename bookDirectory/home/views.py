from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Booklist

# Create your views here.

def index(request):
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
