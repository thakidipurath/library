from django.db import models

# Create your models here.
class Districts(models.Model):
    dis_name=models.CharField(max_length=120)
    population=models.PositiveIntegerField()
    first_dosevr =models.PositiveIntegerField()
    second_dosevr=models.PositiveIntegerField()
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.dis_name


#orm queries for creating a new districts
#     dis=Districts(dis_name="abc",population=500000,first_dosevr=600, second_dosevr=700)
#     dis.save()

# orm queries for listing all districts
# dis=Districts.objects.all()
# dis

# orm query for listing all districts whose second_dosev grater than 800
# dis=Districts.objects.filter(second_dosevr__gt=800)
# dis


# U>>Update

# update the population of palakade to 600000
# dis=Districts.objects.get(id=5)
# dis
# orm query for districts palakade
# dis.dis_name
# orm query for districts palakade population to 600000
# dis.population=600000
# dis.save()
# dis=Districts.objects.get(id=3)
# dis
# dis.dis_name
# update the name of the district ernakulam to kochi
# dis.dis_name="kochi"
# dis.save()



#  Aggregate function


# eg:max,min,average e.t.c
# we need to import these aggregate functions
# from django.db.models import Avg,Sum,Count,Max,Min

# find the highest population from the districts
# from django.db.models import Max

# dis_highpop=Districts.objects.all().aggregate(Max("population"))
# dis_highpop
# find the highest vaccination rate
# dis_hvr=Districts.objects.all().aggregate(Max("first_dosevr"))
# dis_hvr
# find the lowest vaccination rate
# from django.db.models import Min
# dis_lvr=Districts.objects.all().aggregate(Min("first_dosevr"))
# dis_lvr