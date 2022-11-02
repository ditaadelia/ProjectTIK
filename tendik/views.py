from django.shortcuts import render, redirect
from tendik.models import Tendik
from tendik.forms import FormTendik
from django.contrib import messages

# Create your views here.

def hapus_tendik(request, id_tendik):
    tendik = Tendik.objects.filter(id=id_tendik)
    tendik.delete()

    messages.success(request, "Data berhasil dihapus")

    return redirect('tendik')

def ubah_tendik(request, id_tendik):
    tendik = Tendik.objects.get(id=id_tendik)
    templates = 'ubah-tendik.html'
    if request.POST:
        form = FormTendik(request.POST, instance=tendik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_tendik', id_tendik=id_tendik)

    else:
        form = FormTendik(instance=tendik)
        konteks ={
            'form':form,
            'tendik':tendik,
        }
    return render(request, templates, konteks)

def tendik(request):
    tendik = Tendik.objects.all()

    context = {
        'educator' : tendik,
    }
    return render(request,"indextendik.html", context)


def tambah_tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tendik.html', konteks)
    else:
        form = FormTendik()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-tendik.html', konteks)