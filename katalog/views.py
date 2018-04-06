from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import RedirectView
from .models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProfileForm, SearchForm, SearchFormPro

## Функция возвращающая страницу каталога анкет.
#
#  Функция получает на входе запрос и возвращает html файл каталога анкет.
def Profile_list(request):
    Profiles = Profile.objects.all().order_by('first_name')
    paginator = Paginator(Profiles, 4)
    page = request.GET.get('page')
    try:
        Profiles= paginator.page(page)
    except PageNotAnInteger:
        Profiles = paginator.page(1)
    except EmptyPage:
        Profiles = paginator.page(paginator.num_pages)
    return render(request, 'svaha/Profiles.html', {'Profiles': Profiles})

## Функция возвращающая страницу простого поиска.
#
#  Функция получает на входе запрос и возвращает html файл простого поиска.
def Search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            Profiles = Profile.objects.filter(gender= form.cleaned_data['gender'], age= form.cleaned_data['age'])
            if Profiles.count() == 0:
                return render(request, 'svaha/empty.html', {'Profiles': Profiles})
            else:
                return render(request, 'svaha/Profiles.html', {'Profiles': Profiles})
    else:
        form = SearchForm()
    return render(request, 'svaha/Search.html', {'form': form})

## Функция возвращающая страницу расширенного поиска.
#
#  Функция получает на входе запрос и возвращает html файл расширенного поиска.
def SearchPro(request):
    if request.method == "POST":
        form = SearchFormPro(request.POST)
        if form.is_valid():
            Profiles = Profile.objects.filter(gender= form.cleaned_data['gender'], age= form.cleaned_data['age'],
            hair= form.cleaned_data['hair'], eye= form.cleaned_data['eye'], education= form.cleaned_data['education'],
            job= form.cleaned_data['job'], children= form.cleaned_data['children'], Tatoo_p= form.cleaned_data['Tatoo_p'])
            if Profiles.count() == 0:
                return render(request, 'svaha/empty.html', {'Profiles': Profiles})
            else:
                return render(request, 'svaha/Profiles.html', {'Profiles': Profiles})
    else:
        form = SearchFormPro()
    return render(request, 'svaha/SearchPro.html', {'form': form})

## Функция возвращающая страницу определенной анкеты.
#
#  Функция получает на входе запрос и pk анкеты и возвращает html файл определенной анкеты.
def Profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'svaha/Profile_detail.html', {'profile': profile})

## Функция удаляющая анкету.
#
#  Функция получает на входе запрос и pk анкеты, удаляющая определенную анкету и возвращает html каталога анкет.
def Profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    return redirect('Profile_list')

## Функция возвращающая страницу с контактами определенной анкеты.
#
#  Функция получает на входе запрос и pk анкеты и возвращает html файл контактов определенной анкеты.
def Profile_kontakts(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'svaha/Profile_kontakts.html', {'profile': profile})

## Функция редактирующая свойства анкеты возвращающая страницу этой анкеты.
#
#  Функция получает на входе запрос и pk анкеты, редактирует свойства определенной анкеты и возвращает html файл определенной анкеты.
def Profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('Profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'svaha/Profile_edit.html', {'form': form})

## Функция добавляющая новую анкету возвращающая страницу новой анкеты анкеты.
#
#  Функция получает на входе запрос, создает новую анкету и возвращает html файл этой анкеты.
def Profile_add(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('Profile_detail', pk=profile.pk)
    else:
        form = ProfileForm()
    return render(request, 'svaha/Profile_add.html', {'form': form})
