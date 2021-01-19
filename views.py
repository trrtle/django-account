# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    ctx = {"section": "dashboard"}
    return render(request, "account/dashboard.html", ctx)
