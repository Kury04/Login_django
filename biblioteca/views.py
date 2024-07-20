from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def libro_lista(request):
    libros = Libro.objects.all()
    return render(request, 'libro_lista.html', {'libros': libros})

def libro_detalle(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libro_detalle.html', {'libro': libro})

def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm()
    return render(request, 'libro_editar.html', {'form': form})

def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_editar.html', {'form': form})

def libro_eliminar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect('libro_lista')