from django.shortcuts import render, get_object_or_404, redirect
from .models import Themes


def home(request):
    return render(request, 'home.html')


def mavzular_list(request):
    themes = Themes.objects.all()
    return render(request, 'mavzular_list.html', {'themes': themes})


def themes_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        mavzular = request.POST['mavzular']
        new_theme = Themes(name=name, mavzular=mavzular)
        new_theme.save()
        return redirect('/mavzular_list/')
    return render(request, 'themes/themes_add.html')


def mavzular_update(request, pk):
    theme = get_object_or_404(Themes, id=pk)
    if request.method == 'POST':
        theme.name = request.POST['name']
        theme.mavzular = request.POST['mavzular']
        theme.save()
        return redirect('/mavzular_list/')
    return render(request, 'themes/mavzu_update.html', {'theme': theme})


def mavzular_delete(request, pk):
    theme_del = get_object_or_404(Themes, id=pk)
    if request.method == 'POST':
        theme_del.delete()
        return redirect('/mavzular_list/', template_name='mavzular_list.html')
    return render(request, 'themes/mavzu_delete.html', {'theme_del': theme_del})
