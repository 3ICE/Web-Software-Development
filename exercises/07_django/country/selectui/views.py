from django.shortcuts import render, get_object_or_404

from countrydata.models import Continent, Country


def show_continent(request, continent_code=None):
    context = {
        "all_continents": Continent.objects.all()
    }
    if continent_code:
        continent = get_object_or_404(Continent, code=continent_code)
        context["continent"] = continent
    #Ajax
    if request.is_ajax():
        name = request.POST.get('name')
        return render(request, "selectui/countrytable.html", context)
    return render(request, "selectui/index.html", context)
