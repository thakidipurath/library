from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from owner.models import Books
from customer.models import Orders
from owner.forms import BookForm
from django.urls import reverse_lazy
# from django.contrib import messages
from owner.decorators import owner_permission_required
from django.utils.decorators import method_decorator
from owner.forms import OrderProcessForm
from django.core.mail import send_mail


# Create your views here.
# def view_books(request):
#     return render(request,"view_books.html")

@method_decorator(owner_permission_required, name='dispatch')
class BookList(ListView):
    model = Books
    context_object_name = "books"
    template_name = "view_books.html"


#     def get(self, request, *args, **kwargs):
#         books = Books.objects.all()
#         context = {"books": books}
#         return render(request, "view_books.html", context)

@method_decorator(owner_permission_required, name='dispatch')
class AddBooks(CreateView):
    model = Books
    form_class = BookForm
    template_name = "add_books.html"
    success_url = reverse_lazy('listbook')

    # def get(self, request, *args, **kwargs):
    #     books = BookForm()
    #     context = {"books": books}
    #     return render(request, "add_books.html", context)
    #
    # def post(self, request, *args, **kwargs):
    #     books = BookForm(request.POST,files=request.FILES)
    #     if books.is_valid():
    #         books.save()
    #         # print(request.POST)
    #         # book_name = books.cleaned_data.get("book_name")
    #         # author = books.cleaned_data.get("author")
    #         # price = books.cleaned_data.get("price")
    #         # copies = books.cleaned_data.get("copies")
    #         # book = Books(book_name=book_name, author=author, price=price, copies=copies)
    #         messages.success(request,"book added")
    #         return redirect("addbook")
    #     else:
    #         context={"books":books}
    #         messages.error(request,"book adding failed")
    #         return render(request, "add_books.html",context)

    #
    # def post(self,request,*args,**kwargs):
    #     # book_name=request.POST["bk_name"]
    #     # author=request.POST["bk_author"]
    #     # price=request.POST["bk_price"]
    #     # copies=request.POST["bk_copies"]
    #     form=BookForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #
    #     return render(request,"add_books.html")


@method_decorator(owner_permission_required, name='dispatch')
class BookDetail(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book_detail.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbook")

    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     detail = Books.objects.get(id=id)
    #     # book=[ book for book in Books if book["id"]==id][0]
    #     context={'book':detail}
    #     return render(request,"book_detail.html",context)


@method_decorator(owner_permission_required, name='dispatch')
class BookDelete(DeleteView):
    model = Books
    template_name = "delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbook")

    # def get(self,request,*args,**kwargs):
    #     id= kwargs ['id']
    #     delete = Books.objects.get(id=id)
    #     delete.delete()
    #     return redirect("listbook")


@method_decorator(owner_permission_required, name='dispatch')
class BookChange(UpdateView):
    model = Books
    form_class = BookForm
    template_name = "book_edit.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("listbook")

    # def get(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     book = Books.objects.get(id=id)
    #
    # dict={"book_name":book.book_name,
    #       "author":book.author,
    #       "price":book.price,
    #       "copies":book.copies,
    #       }
    #     form=BookForm(instance=book)
    #     context={"form":form}
    #     return render(request,"book_edit.html",context)
    #
    # def post(self, request, *args , **kwargs):
    #     id= kwargs['id']
    #     book = Books.objects.get(id=id)
    #     edit= BookForm(request.POST,instance=book,files=request.FILES)
    #     if edit.is_valid():
    #         edit.save()
    #         return redirect("listbook")

    #    book=[ book for book in books if book["id"]==id][0]
    #    form = BookeditForm(initial={"book_name":book["book.name"],"author":book["author"],"price":book["price"],"copies":book["copies"]})
    #    form=BookForm(initial=books)
    #    return render(request,"book_edit.html",{"form":form})


class OwnerDashView(ListView):
    model = Orders
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        order = self.model.objects.filter(status="orderplaced")
        context = {"order": order}
        return render(request, self.template_name, context)


class OrederDetail(DetailView):
    model = Orders
    template_name = "order_detail.html"
    pk_url_kwarg = 'id'
    context_object_name = "order"







class OrderProcessView(UpdateView):
    model = Orders
    form_class = OrderProcessForm
    pk_url_kwarg = "id"
    template_name = "order_process.html"
    success_url = reverse_lazy("dashbors")

    def form_valid(self, form):
        self.object = form.save()
        order=self.object
        print("usernnnnnnnnnnnnnnnnnnnn",order.user.email)
        expected_delivery_date = form.cleaned_data.get("expected_delivery_date")
        send_mail(
            'Book order conformation',
            'Your product has been delivered on ' + str(expected_delivery_date),
            'jeevanthomas2021@gmail.com',
            ['bworld634@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)
