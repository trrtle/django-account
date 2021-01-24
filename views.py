# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from account.forms import UserRegistrationForm


@login_required
def dashboard(request):
    ctx = {"section": "dashboard"}
    return render(request, "account/dashboard.html", ctx)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(
                request, 'account/register_done.html', {'new_user': new_user}
            )
    else:
        user_form = UserRegistrationForm()
        return render(
            request, 'account/register.html', {'user_form': user_form}
        )
