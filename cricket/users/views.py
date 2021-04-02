from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from.models import Profile
from.models import runs
from.models import wickets
from.forms import ProfileForm
from.forms import RunsForm
from.forms import WicketsForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has bee created! You are now able to Login {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html' )

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('users/logout.html')

@login_required
def edit_profile (request):
    if request.method == 'GET':

            return render(request,'users/edit_profile.html',{'form':ProfileForm()})
    else:
        form = ProfileForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_UserProfileForm = form.save(commit=False)
            new_UserProfileForm.user = request.user
            new_UserProfileForm.save()
        return render(request,'users/profile.html',{'form':ProfileForm()})

@login_required
def runs_form(request):
    if request.method == 'GET':
        return render(request,'users/batsman_form.html',{'form':RunsForm()})
    else:

        form = RunsForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_UserRunsForm = form.save(commit=False)
            new_UserRunsForm.user = request.user
            new_UserRunsForm.save()
        return redirect('runs_list')


def runs_list(request):
    context ={'runs_list': runs.objects.all()}
    return render(request,"users/batsman_list.html",context)


@login_required
def runs_delete(request,runs_id):
    delete_runs = get_object_or_404(runs,pk=runs_id)
    if request.method == 'POST':
        delete_runs.delete()
        messages.success(request, 'Succesfuly Deleted', extra_tags='alert')
        return redirect('runs_list')


@login_required
def wickets_form(request):
    if request.method == 'GET':
        return render(request,'users/bowlers_form.html',{'form':WicketsForm()})
    else:

        form = WicketsForm(request.POST,request.FILES or None)
        if form.is_valid():
            new_UserRunsForm = form.save(commit=False)
            new_UserRunsForm.user = request.user
            new_UserRunsForm.save()
        return redirect('wickets_list')


def wickets_list(request):
    context ={'wickets_list': wickets.objects.all()}
    return render(request,"users/bowlers_list.html",context)


@login_required
def wickets_delete(request,wickets_id):
    delete_wickets = get_object_or_404(wickets,pk=wickets_id)
    if request.method == 'POST':
        delete_wickets.delete()
        messages.success(request, 'Succesfuly Deleted', extra_tags='alert')
        return redirect('wickets_list')
