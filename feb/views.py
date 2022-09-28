from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'feb\index.html', konteks)
