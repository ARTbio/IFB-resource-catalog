from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return render(request, 'database/portal.html')


    return HttpResponse("Welcome to the Catalogue of French resources in bioinformatics")

