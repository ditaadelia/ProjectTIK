from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fk\index.html', konteks)
