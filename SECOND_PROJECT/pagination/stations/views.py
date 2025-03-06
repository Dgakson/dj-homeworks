from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    station_list = []
    with open('data-398-2018-08-30.csv', mode='r', encoding='utf-8') as file:
        # Создаем объект DictReader
        reader = csv.DictReader(file)
        for row in reader:
            station_list.append(row)

    paginator = Paginator(station_list, 5)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)
