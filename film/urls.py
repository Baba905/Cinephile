from django.urls import include, path
from film import views
urlpatterns = [
    path('',views.search, name='search'),
    path('categories', views.categories, name='categories'),
    path('details-film/<int:id>', views.detail_film, name='details-film'),
]
