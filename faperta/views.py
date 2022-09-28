from django.shortcuts import render

# Create your views here.
def prodi1(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'faperta\index.html', konteks)
