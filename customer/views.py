from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, ListView, DeleteView, CreateView, TemplateView
# from customer.forms import FeedbackForm
from customer.forms import UserRegistrationForm, LoginForm, OrderForm
from owner.models import Books
from django.contrib.auth import authenticate, login, logout
from customer.decorators import sign_in_required
from django.utils.decorators import method_decorator
from customer.models import Carts
from customer.models import Orders
from django.db.models import Sum
from customer.filters import BookFilter
from customer.models import Profile
from customer.forms import ProfileForm
from django.urls import reverse_lazy


# Create your views here.

# def index(request):
#     return render(request,"index.html")
#
# def view_my_cart(request):
#     return render(request,"view_my_cart.html")
#  #   return HttpResponse("<h1>customer carts</h1>")
#
# def view_my_orders(request):
#     return render(request,"view_my_orders.html")
#   #  return HttpResponse("<h1>customer order</h1>")
#@method_decorator(sign_in_required, name='dispatch')
class CustmerHome(View):
    def get(self, request, *args, **kwargs):
        books = Books.objects.all()
        filter = BookFilter(request.GET, queryset=Books.objects.all())
        context = {"books": books, "filter": filter}
        return render(request, "home_customer.html", context)


# class FeedbackView(View):
#     def get(self, request, *args, **kwargs):
#         form = FeedbackForm()
#         context = {"form": form}
#         return render(request, "add_feedback.html", context)
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return render(request, "add_feedback.html")

class SignupView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form}
        return render(request, "signup.html", context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user created")
            return redirect("signip.html")
        else:
            context = {"form": form}
            return render(request, "signup.html", context)


class SigninView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "signip.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("here")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("listbook")
                else:
                    return redirect("custhome")

            else:
                context = {"form": form}
                return render(request, "signip.html", context)
        else:
            context = {"form": form}
            return render(request, "signin.html", context)


def sign_out(request):
    logout(request)
    return redirect("signin")


class Addtocart(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        book = Books.objects.get(id=id)
        user = request.user
        carts = Carts(user=user, item=book)
        carts.save()
        print('item has been added')
        return redirect('custhome')


class CartItems(ListView):
    model = Carts
    template_name = "cartitem.html"
    context_object_name = "items"

    # def get_queryset(self):
    #     return self.model.objects.filter(user=self.request.user)
    def get(self, request, **kwargs):
        logeduser = self.model.objects.filter(user=self.request.user, status="incart")

        total_sum = logeduser.aggregate(Sum("item__price"))
        total = total_sum["item__price__sum"]

        context = {"items": logeduser, "total": total}
        return render(request, self.template_name, context)


class RemoveCsrtItem(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        cart = Carts.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        return redirect("cartitem")


class OrderView(CreateView):
    model = Orders
    template_name = "customer_orders.html"
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        p_id = kwargs.get("p_id")
        c_id = kwargs.get("c_id")
        form = OrderForm(request.POST)
        if form.is_valid():
            book = Books.objects.get(id=p_id)
            cart = Carts.objects.get(id=c_id)
            address = form.cleaned_data.get("address")
            user = request.user
            order = Orders(user=user, address=address, item=book)
            order.save()
            cart.status = "order_placed"
            cart.save()
            return redirect("custhome")


class MyOrders(ListView):
    model = Orders
    template_name = "my_orders.html"
    context_object_name = "order"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).exclude(status="cancel")


def cancell_order(request, *args, **kwargs):
    o_id = kwargs.get("o_id")
    cancell = Orders.objects.get(id=o_id)
    cancell.status = "cancel"
    cancell.save()
    return redirect("myorder")


class ProfileView(CreateView):
    model = Profile
    template_name = "cust_profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("custhome")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect("custhome")
        else:
            return render(request,self.template_name,{"form":form})


class ViewMyProfile(TemplateView):
    template_name = "my_profile.html"
# class RegistrationView(View):
#     def get(self, request):
#         form = RegistrationForm()
#         context = {"form": form}
#         return render(request, "registration.html", context)

# def post(self, request):
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#         print(form.cleaned_data)
#         return render(request, "registration.html")
