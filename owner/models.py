from django.db import models

# Create your models here.

# books=[
#     {"id": 100,"book_name":"randamoozham","author":"mt","price":480,"copies":250},
#     {"id":101,"book_name": "aarachar", "author": "meera", "price": 580, "copies": 250},
#     {"id":102,"book_name": "the alchemist", "author": "paulo", "price": 780, "copies": 250},
#     {"id":103,"book_name": "rainrising", "author": "nirupama", "price": 1000, "copies": 250},
#     {"id":104,"book_name": "indhuleka", "author": "chandhu menon", "price": 280, "copies": 250},
#     {"id":105,"book_name": "pazhassy", "author": "mt", "price": 580, "copies": 350},
#
# ]

class Books(models.Model):
    book_name=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    active_status = models.BooleanField(default=True)
    images=models.ImageField(upload_to="image",null=True,blank=True)


    def __str__(self):
        return self.book_name

    # ORM queries
    # CRUD
    #
    # C>>Create
    #     book=Books(book_name="abc",author="abc", price=50000,copies=5)
    #     book.save()
    # refname=Modelname(field_name=value,field_name=value,,,,,,)
    # refname.save()
    # book=Books(book_name="randamoozham",author="mt",price="450",copies="10")
    # book.save()

    # R>>Retrieve
    # Select all books from our model
    # refname=modelname.objects.all()
    # book=Books.objects.all()

    # ORM queries
    #

    # print all book details available under 600
    #book = Books.objects.filter(price__lt=600)
    #book

    # print all book details available under range of 400 to 500
    # book = Books.objects.filter(price__gt=400,price__lt=500)
    # book

    # print all book details of the book Induleka
    # book = Books.objects.get(id=5)
    # book
    # print(book.book_name,book.author,book.price,book.copies)

    # print all book whose copies is greater than 30
    #book = Books.objects.filter(copies__gt=30).count()
    #book

    # print all the inactive books
    # book = Books.objects.filter(active_status=False)
    # book
    # only book names
    # bookname = Books.objects.filter(active_status=False).values("book_name")
    # bookname

    #  Aggregate function

    # eg:max,min,average e.t.c
    # we need to import these aggregate functions
    # from django.db.models import Avg,Sum,Count,Max,Min

    # find the book with the highest price
    # find the book with the lowest price
