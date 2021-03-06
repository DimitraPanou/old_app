from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.db import IntegrityError, transaction

from .decorators import unauthenticated_user

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request,'Please correct the error below.')    

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def users_all(request):
    users = Profile.objects.all()
    #for 
    #groups = User.objects.groups.all()
    return render(request, 'users/users_all.html', {
        'users': users
    })

@login_required
#@transaction.atomic
def test(request):

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    print(u_form)
    print(p_form)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/test.html', context)
#class Profile(DetailView):
#	template_name='users/profile.html'
#	queryset = User.objects.all()

#	def get_object(self):
#		id_ = self.kwargs.get()

#ALTER USER postgres PASSWORD 'dim123!@#';
#CREATE ROLE DK_LAB LOGIN SUPERUSER PASSWORD 'DKontogiann1s';