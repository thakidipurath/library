from api import views
from django.urls import path

urlpatterns=[
    path('book/',views.BooksView.as_view()),
    path('book/<int:id>',views.BookDetailsView.as_view()),

]