import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from car.forms import CarForm
from car.models import Car


def index(request):
    return render(request,'home.html')

def list_cars(request):
    cars = Car.objects.all()
    return render(request,'car_list.html',{'cars':cars})

def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list-cars')
    else:
        form = CarForm()
        return render(request,'car_creation_form.html',{'form':form})

def update_car(request,id):
    car = get_object_or_404(Car, id=id)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('list_cars')
    else:
        form = CarForm(instance=car)
        return render(request, 'update_car.html', {'form': form})

def car_detail(request,pk):
    car = Car.objects.get(id=pk)
    form = CarForm(instance=car)
    return render(request,'car_detail.html',{'form':form,'car':car})

def delete_car(request,pk):
    car = Car.objects.get(id=pk)
    if car:
        car.delete()
        return HttpResponseRedirect('/list-cars')
    else:
        return HttpResponseRedirect('/list-cars',status=400)