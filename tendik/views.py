from django.shortcuts import render
from tendik.models import Tendik

# Create your views here.

def tendik(request):

    context = {
        'educator': Tendik.objects.all()
    }    
    return render(request, 'indextendik.html', context)