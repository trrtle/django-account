# from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from account.forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile

User = get_user_model()


@login_required
def dashboard(request):
    ctx = {"section": "dashboard"}
    return render(request, "account/dashboard.html", ctx)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {"new_user": new_user})

    user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error update your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    ctx = {"user_form": user_form, "profile_form": profile_form}
    return render(request, "account/edit.html", ctx)


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    ctx = {"section": "people", "users": users}
    return render(request, "account/user/list.html", ctx)


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    ctx = {"section": "people", "user": user}
    return render(request, "account/user/detail.html", ctx)
