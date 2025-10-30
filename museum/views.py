from django.shortcuts import render

def home(request):
    return render(request, 'museum/index.html')

def visit(request):
    return render(request, 'museum/visit.html')

def history(request):
    return render(request, 'museum/history.html')

def art(request):
    return render(request, 'museum/art.html')

def archbold(request):
    return render(request, 'museum/archbold.html')

def springfieldforward(request):
    return render(request, 'museum/springfieldforward.html')

def contact(request):
    return render(request, 'museum/contact.html')