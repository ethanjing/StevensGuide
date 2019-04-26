from django.shortcuts import render, redirect
from .models import Restaurant, Comment, Wishlist
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm, ProfileForm, CommnetForm
from django.urls import reverse


def index(request):
    userExist = False
    if request.user.is_authenticated:
        userExist = True
    return render(request, "index.html", context={'userExist': userExist})


@login_required
def user_profile(request):
    user = request.user
    wishlist = Wishlist.objects.filter(user=user)
    if not wishlist:
        existwishlist = False
    else:
        existwishlist = True
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

    return render(request, "userProfile.html", context={'form': form, 'existwishlist': existwishlist,
                                                        'userExist': True, 'wishlist': wishlist})


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
    url = reverse("restaurantdetail", args=[rid])
    try:
        restaurant = Restaurant.objects.get(id=rid)
        comments = Comment.objects.filter(restaurant=restaurant)
    except Restaurant.DoesNotExist:
        raise Http404("Restaurant does not exist")
    except Comment.DoesNotExist:
        comments = None
    enablecomment = False
    if request.user.is_authenticated:
        userExist = True
        enablecomment = True
        if request.method == 'POST':
            form = CommnetForm(request.POST)
            if form.is_valid():
                newcomment = Comment()
                newcomment.restaurant = restaurant
                newcomment.user = request.user
                newcomment.comment = form.cleaned_data['commenttext']
                newcomment.save()

                return redirect(reverse("restaurantdetail", args=[rid]))

    return render(request, "restaurantDetail.html", context={'restaurant': restaurant,
                                                             'comments': comments,
                                                             'enablecomment': enablecomment,
                                                             'userExist': userExist,
                                                             'url': url, })
