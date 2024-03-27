from django.shortcuts import render

# Create your views here.
#business logic here

def Welcome(request):
    return render(request, 'index.html')


