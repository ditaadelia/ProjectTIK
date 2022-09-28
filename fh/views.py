from django.shortcuts import render

# Create your views here.
def prodi3(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fh\index.html', konteks)
