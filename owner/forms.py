from django.forms import ModelForm
from django import forms
from owner.models import Books
from customer.models import Orders


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = "__all__"
        # exclude=("active_status",)
        widgets = {
            "book_name": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),
            "images": forms.FileInput(attrs={"class": "form-control"}),

        }


class OrderProcessForm(ModelForm):
    class Meta:

        model = Orders
        fields = ["status", "expected_delivery_date"]

        widgets = {
              "status": forms.Select(attrs={"class": "form-control"}),
              "expected_delivery_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }

# class BookForm(forms.Form):
#     book_name=forms.CharField()
#     author=forms.CharField()
#     price=forms.CharField()
#     copies=forms.CharField()
