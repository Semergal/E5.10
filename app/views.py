from django.shortcuts import render

# Create your views here.
from .models import Car
from django.views.generic import ListView
from django.db.models import Q
from django.db.models.query_utils import Q

class CarFilter:

    def get_car(self):
        return Car.objects.all()

#класс списка автомобилей
class CarList(CarFilter, ListView):
    model = Car
    template_name = 'cars.html'

#класс фильтрайии
class FilterCarView(CarList, ListView):

    def get_queryset(self):
        queryset = Car.objects.filter(
            Q(manufacturer__in=self.request.GET.getlist('manufacturer')) |
            Q(transmission__in=self.request.GET.getlist('transmission'))
        )
        return queryset