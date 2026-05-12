from django.shortcuts import render , redirect
from .forms import LibraryForm
from .models import Library
from django.contrib.auth.decorators import login_required
from .serializers import LibrarySerializer
from rest_framework import viewsets

@login_required()
def add_barrow(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lib_home')
    else:
        form = LibraryForm()

    return render(request, 'library/add_barrow.html', {'form': form})

@login_required()
def index(request):
    obj = Library.objects.all()
    return render(request, 'library/home.html', {'obj': obj})

@login_required()
def edit_barrow(request , library_id):
    obj = Library.objects.get(pk=library_id)
    form = LibraryForm(instance=obj)
    if request.method == 'POST':
        form = LibraryForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect('lib_home')
    return render(request, 'library/add_barrow.html', {'form': form})

@login_required()
def delete_barrow(request , library_id):
    obj = Library.objects.get(pk=library_id)
    obj.delete()
    return redirect('lib_home')

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer




