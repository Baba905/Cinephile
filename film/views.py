from cgitb import reset
from tkinter import SE
from django.http import HttpResponse
from django.shortcuts import render
from film.forms import Search
import requests


def search(request):
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            print("formulaire marche")
            query = form.cleaned_data['search']
            print(query)
            data = requests.get(
                f"https://api.themoviedb.org/3/search/movie?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US&query={query}&page=1&include_adult=false", verify=False)
            return render(request, 'search.html', {'data': data.json()})
        else:
            return HttpResponse("Formulaire non valide")
    else:
        form = Search()
        return render(request, 'base.html', {'form': form})

# def categories(request):
#     categories = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af").json()
#     return render(request,'home.html', {'categories': categories})


def detail_film(request, id):
    details = requests.get(
        f"https://api.themoviedb.org/3/movie/{id}?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US").json()
    return render(request, 'film_details.html', {'details': details})


def films_par_categories(request, id):
    films = requests.get(
        f"https://api.themoviedb.org/3/discover/movie?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US&sort_by=popularity.desc&include_adult=false&page=1&with_genres={id}").json()
    return render(request, "home.html", {'films': films})


def accueil(request, page):
    default_data = requests.get(
        f"https://api.themoviedb.org/3/discover/movie?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US&include_adult=false&include_video=false&page={page}&with_genres=&with_watch_monetization_types=flatrate")
    return render(request, 'home.html', {"default": default_data.json()})


def page_categorie(request, id_categorie):
    cat_data = requests.get(
        f"https://api.themoviedb.org/3/discover/movie?api_key=d8bcd4f8c9cf9fe1e3864fc180fb62af&language=en-US&include_adult=false&include_video=false&page=1&with_genres={id_categorie}&with_watch_monetization_types=flatrate")
    return render(request, 'categorie_page.html', {'categorie_data': cat_data.json()})
