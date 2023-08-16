from django.shortcuts import render
from django.http import HttpResponse
from .models import Breakfast




def dashboard(request):
    return render(request, 'dashboard.html')



def breakfast(request):
    return render(request, 'breakfast.html')




def save(request):
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        calories = request.POST.get('calories')
        carbs = request.POST.get('carbs')
        protein = request.POST.get('protein')
        fat = request.POST.get('fat')
        print(item_name, calories, carbs, protein, fat)
        # save data to model
        breakfast = Breakfast(item_name=item_name, calories=calories, carbs=carbs, protein=protein, fat=fat)
        breakfast.save()
        return HttpResponse("Data saved successfully")