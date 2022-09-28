from django.shortcuts import render

# Create your views here.
def univ(request):
    judul = ["Ilmu Hukum"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'univ.html', konteks)
