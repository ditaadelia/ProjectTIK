from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'ft\index.html', konteks)
