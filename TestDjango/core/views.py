from django.shortcuts import render
# Create your views here.

def indexV3(request):
    return render(request, 'core/indexV3')
