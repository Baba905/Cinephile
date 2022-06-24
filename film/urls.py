from django.urls import include, path
from film import views
urlpatterns = [
    path('accueil/<int:page>',views.accueil, name='accueil'),
    path('categories/<int:id_categorie>', views.page_categorie, name='categorie_page'),
    path('details-film/<int:id>', views.detail_film, name='details-film'),
]
