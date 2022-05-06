from owner import views
from django.urls import path

urlpatterns=[
    path("books/all",views.BookList.as_view(),name="listbook"),
    path("books/add",views.AddBooks.as_view(),name="addbook"),
    path("books/<int:id>",views.BookDetail.as_view(),name="bookdetail"),
    path("books/change/<int:id>",views.BookChange.as_view(),name="bookedit"),
    path("book/delete/<int:id>",views.BookDelete.as_view(),name="delete"),
    path("order/dashbord",views.OwnerDashView.as_view(),name="dashbors"),
    path("order/view/<int:id>",views.OrederDetail.as_view(),name="fulldetails"),
    path("order/details/<int:id>",views.OrderProcessView.as_view(),name="details"),
]