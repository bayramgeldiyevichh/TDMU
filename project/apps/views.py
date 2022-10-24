import email
from logging.config import IDENTIFIER
from multiprocessing import context
from operator import sub
from unicodedata import category, name
from xml.dom.minidom import Identified
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login, authenticate, logout as logout 
from django.contrib import messages
from .forms import CreateUserForm
from .forms import*
from .models import *
from django.http import HttpResponse


subcatarr = []


# @login_required(login_url='sign_in')
def index(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }

    return render(request, 'index.html', context)


# @login_required(login_url='sign_in')
def sub_category(request, id):
    sub_category = SubCategory.objects.filter(cat_id=id)

    for s in sub_category:
        subcatarr.append(s.id)

    context ={
        'sub_category':sub_category
    }

    return render(request, 'pars/basgancak.html', context)



# @login_required(login_url='sign_in')
def soraglar(request, id):
    sorag = Questions.objects.filter(sub_question=id)
    sub_category = SubCategory.objects.filter(id=id)
    # print(sub_category)


    # sorag = soraglar
    # for s in sorag:
    #     subcatarr.append(s.id)

    # print(subcatarr)

    context ={
        'sorag':sorag,
        'sub_category':sub_category
    }

    return render(request, 'pars/sorag/soraglar.html', context)




def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Üstünlikli amala aşyryldy' + user)
                return redirect('sign_in')
            else:
                messages.info(request, 'e-mail pocta öň registrasiýa edilen')
        return render(request, 'register/sign_up.html', {'form': form})



def sign_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            email = authenticate(email=email, password=password)

            if email is not None:
                login(request,email)
                return redirect('index')
            else:
                messages.info(request, 'Ulanyjy email poctasy ýa-da paroly nädogry')
        context = {}
        return render(request, 'register/sign_in.html', context)


def logout(request):
    django_logout(request)
    return redirect('index')


# @login_required(login_url='sign_in')
def profile_register(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    return render(request, 'profile_register.html', {'form': form})


# @login_required(login_url='sign_in')
def profile_page(request):
    profile = Profile.objects.get(user=request.user.id)
    return render(request, 'profile_page.html', {'profile': profile})


def profile_setting(request):
    profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    return render(request, 'profile_register.html', {'form': ProfileForm(instance=profile)})



def statistika(request):
    user = request.user
    dogry = request.GET['d']
    yalnys = request.GET['y']
    sub_id = request.GET['sub_id']
    sub_category = SubCategory.objects.get(id=sub_id)

    user_category = CategoryUser.objects.filter(user_id=user, sub_category_id=sub_category).first()
    if user_category:
        user_category.dogry_jogap = dogry
        user_category.yalnysh_jogap = yalnys
        user_category.save()
    else:
        jogaplar = CategoryUser.objects.create(user_id=user, dogry_jogap=dogry, yalnysh_jogap=yalnys, sub_category_id=sub_category)
        
        jogaplar.save()
    
    return redirect('/')
    # return render(request, 'pars/basgancak.html')




@login_required(login_url='sign_in')
def sub_cat_percent(request, id):
    sub_cat = SubCategory.objects.filter(cat_id=id)
    # sub_cat = sub_cat.count()
    # print(sub_cat)
    total_questions = 0
    for sub in sub_cat:
        questions = Questions.objects.filter(sub_question=sub)
        qcount = questions.count()
        total_questions += qcount
    
    user = request.user
    cat_user = CategoryUser.objects.filter(user_id=user)
    cat_user_id = cat_user.filter(sub_category_id__cat_id=id)
    total_correct = 0
    for c in cat_user_id:
        total_correct += int(c.dogry_jogap)


    # print(total_questions)
    # print(total_correct)
    if total_correct  == 0 or total_questions == 0:
        total = 0
    else:
        total =  total_correct * 100 // total_questions
    
    print(total)

    context = {
        'sub_cat':sub_cat,
        'cat_user':cat_user,
        'cat_user_id':cat_user_id,
        'total': total
    }
    return render(request, 'pars/basgancak.html', context)


