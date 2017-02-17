# My #1 advice to all classmates: fix your indentation. Tabs/spaces are NOT interchangeable, one space is confusing, just use four spaces everywhere... I've helped five people with this rookie mistake. And made this mistake myself several times.
#2: If you use PyCharm or any proper IDE it does syntax check and code auto completion for you.
from django.http import Http404, HttpResponse
from .models import Continent, Country


def continent_json(request, continent_code):
    data = Continent.objects.filter(code__exact=continent_code)
    if not data:
        raise Http404("Not found")
    r = ""
    if request.GET.get('callback', '') != '':
        # myCallbackFunction(
        r += request.GET.get('callback') + "("
    # {"xk": "Kosovo","ch": "Switzerland","gr": "Greece","gb": "United Kingdom"}
    r += "{"
    for country in data[0].countries.all():
        r += '"' + country.code + '":"' + country.name + '",'
    # 3ICE: Remove last comma
    r = r[:-1]
    r += "}"
    if request.GET.get('callback', '') != '':
        r += ")"
        return HttpResponse(r, content_type="application/javascript")

    return HttpResponse(r, content_type="application/json")


def country_json(request, continent_code, country_code):
    d = Country.objects.filter(code__exact=country_code)
    if not d:
        raise Http404("Not found")
    d=d[0]
    if d.continent.code != continent_code:
        raise Http404("Wrong continent")
    # {"area": 337030,"population": 5244000,"capital": "Helsinki"}
    r = '{"area":' + str(d.area) + ', "population":' + str(d.population) + ',"capital":"' + d.capital + '"}'
    if request.GET.get('callback', '') != '':
        # r = '%s(%s);' % (request.REQUEST['callback'], r)
        r = request.GET.get('callback', '') + '(' + r + ')'
        return HttpResponse(r, content_type="application/javascript")
    # return JsonResponse(Country.objects.filter(code__exact=continent_code))
    return HttpResponse(r, content_type="application/json")
