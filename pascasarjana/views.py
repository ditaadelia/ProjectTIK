from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'pascasarjana\index.html', konteks)
