from django.shortcuts import render

# IMPORTADO POR MIM
from django.http import HttpResponse


def home(request):
    return render(request, "todos/index.html")
