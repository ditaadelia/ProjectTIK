from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fKIP\index.html', konteks)
