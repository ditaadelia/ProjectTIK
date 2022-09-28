from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'fisip\index.html', konteks)
