from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import MovieForm

# Create your views her
def index(request):
    Movie=movie.objects.all()
    context={
        'movie_list':Movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'Movie':Movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        year=request.POST.get('year')
        img=request.FILES['img']
        Movie=movie(name=name,description=description,year=year,img=img)
        Movie.save()

    return render(request,'add.html')

def update(request,id):
    mvi=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=mvi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'mvi':mvi})

def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')
