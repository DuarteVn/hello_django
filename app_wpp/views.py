from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    
    return HttpResponse('<h1> A soma de {} e {}</h1>'.format(nome, idade))
