from django.shortcuts import render, redirect
from .models import Restaurant, Comment
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, ProfileForm
from django.urls import reverse


def index(request):
    userExist = False
    if request.user.is_authenticated:
        userExist = True
    return render(request, "index.html", context={'userExist': userExist})


@login_required
def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse("profile"))
    else:
        form = ProfileForm(initial={'username': user.username,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'email': user.email})

    return render(request, "userProfile.html", context={'form': form, 'existwishlist': False, 'userExist': True})


def user_signup(request):
    if request.user.is_authenticated:
        return redirect(reverse("profile"))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data.get("username")
            #raw_password = form.cleaned_data.get("password1")
            #user = authenticate(username=username, password=raw_password)
            user = form.save()
            login(request, user)
            return redirect(reverse("profile"))
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", context={'form': form, 'userExist': False})


def restaurant_list(request):
    userExist = False
    if request.user.is_authenticated:
        userExist = True
    restaurants = Restaurant.objects.all()
    return render(request, "restaurantList.html", context={'restaurants': restaurants, 'userExist': userExist})


def restaurant_detail(request, rid):
    userExist = False
    try:
        restaurant_id=Restaurant.objects.get(id=rid)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    enablecomment = False
    if request.user.is_authenticated:
        userExist = True
        uid = request.user.get_profile().id
        comment = Comment.object.filter(restaurant=rid, user=uid)
        if comment is None:
            enablecomment = True

    restaurant = Restaurant.objects.filter(id=rid)
    comments = Comment.objects.filter(restaurant=rid)
    return render(request, "restaurantDetail.html", context={'restaurant': restaurant,
                                                             'comments': comments,
                                                             'enablecomment': enablecomment,
                                                             'userExist': userExist})
