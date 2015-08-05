from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return HttpResponseRedirect(
                reverse("signup_ok")
            )
    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, "registration/signup.html", {
        "userform": userform,
    })

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def question(request):
    return render(request, "question.html")

def login(request):
    return render(request, "registration/login.html")
