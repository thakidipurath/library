import django_filters
from owner.models import Books

class BookFilter(django_filters.FilterSet):
    class Meta:
        model= Books
        fields={"book_name":["contains"],
                "author":["contains"],
                "price":["lt"],
                }
        # widgets = {
        #     "book_name": form.TextInput(attrs={"class": "form-control"}),
        #     "author": fields.TextInput(attrs={"class": "form-control"}),
        #     "price": fields.TextInput(attrs={"class": "form-control"}),
        #
        # }