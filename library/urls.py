"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user.views import login_view, logout_view, register_view
from genre.views import (
    genres as genres_view,
    genre as genre_view,
    add_genre, edit_genre
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # user app
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='registration'),
    path('genres/', genres_view, name='genres'),
    path('genre/<int:genre_id>/', genre_view, name='genre'),
    path('add_genre/', add_genre, name='add_genre'),
    path('edit_genre/<int:genre_id>/', edit_genre, name='edit_genre'),
]
