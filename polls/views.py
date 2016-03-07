from django.shortcuts import render
from polls.models import Person


def people(request):
    return render(request, "people.html", {"people": Person.objects.all()})
