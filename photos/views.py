from django.http import HttpResponseRedirect
from django.shortcuts import render

from photos.forms import SearchForm
from photos.models import Category, Photos


def index(request):
    categories = Category.objects.all()
    photos = Photos.objects.all()
    return render(request, 'index.html', {'categories': categories, 'photos': photos})


def category_photos(request, pk):
    categories = Category.objects.all()
    catdata = Category.objects.get(pk=pk)
    photos = Photos.objects.filter(category_id=pk)
    context = {
        'categories': categories,
        'catdate': catdata.name,
        'photos': photos,
    }

    return render(request, 'category_photos.html', context)


def photos_detail(request, pk):
    categoies = Category.objects.all()
    photos = Photos.objects.get(pk=pk)
    context = {'categories': categoies, 'photos': photos}
    return render(request, 'photos_detail.html', context)


def search(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                photos = Photos.objects.filter(title__icontains=query)
            else:
                photos = Photos.objects.filter(title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {'photos': photos,
                       'query': query,
                       'category': category,
                       'categories': categories}
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')
