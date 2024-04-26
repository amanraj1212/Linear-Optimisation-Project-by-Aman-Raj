#views.py
# ga_app/views.py

from django.shortcuts import render
from .genetic_algorithm import genetic_algorithm

def home(request):
    if request.method == 'POST':
        target = request.POST.get('target', '')
        mutation_rate = float(request.POST.get('mutation_rate', '0.03'))
        population_size = int(request.POST.get('population_size', '500'))
        max_generations = int(request.POST.get('max_generations', '1000'))

        result = genetic_algorithm(target, mutation_rate, population_size, max_generations)

        return render(request, 'ga_app/home.html', {'result': result})

    return render(request, 'ga_app/home.html')

