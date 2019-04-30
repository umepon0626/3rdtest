from django.shortcuts import render


def index(request):
    return render(request, 'e_journal/index.html')
    
