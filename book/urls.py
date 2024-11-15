from django.urls import path
from . import views

urlpatterns=[
    path("bookhome",views.bookhome,name='bookhome'),
    path('<int:book_id>', views.bookdetail, name='bookdetail'),
     path('<int:book_id>/createbookreview', views.createbookreview, name='createbookreview'),
]