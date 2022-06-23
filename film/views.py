from django.http import HttpResponse
from django.shortcuts import render
import requests

def search(request):
    query = request.GET.get('q')
    print("Query set")
    if True:
        print("Query work")
        data = requests.get("https://api.themoviedb.org/3/search/movie?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US&query=harry&page=1&include_adult=false", verify=False)
        return render(request, "home.html", {'data': data.json()})
    else: 
        print("Query don't")
        return HttpResponse("Not found")

def categories(request):
    categories = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af").json()
    return render(request,'home.html', {'categories': categories})

def detail_film(request,id):
    details = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US").json()
    return render(request,'home.html', {'details':details})