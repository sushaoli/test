from django.shortcuts import render_to_response
from menu.models import *
# Create your views here.
def display(foods):
    display_list = []

    for food in foods:
        display_list.append(food.title)

        children = food.children.all()
        if len(children) > 0:
            display_list.append(display(food.children.all()))
    return display_list


def unordered_list(request):
    foods = Food.objects.filter(parent=None)
    var = display(foods)

    return render_to_response('unordered_list.html', {'var': var})