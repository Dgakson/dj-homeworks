import os

from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1222,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
}


def home_view(request):

    template_name = 'home.html'
    pages = {'Главная страница': reverse('home')}
    for d in DATA:
        pages[f'Список продуктов для {d.upper()}'] = d

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def recipe(request, name):
    servings = int(request.GET.get('servings', 1))
    template_name = 'index.html'
    recipe =  DATA[name]
    recipe = {key: round(value * servings, 2) for key, value in recipe.items()}
    context = {
        'recipe': recipe,
        'servings': servings
    }
    return render(request, template_name, context)