from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', dict(response=request.POST.get('input')))
