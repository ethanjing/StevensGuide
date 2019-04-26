from django.urls import path
from django.conf.urls import include
from .views import index, user_signup, user_profile, restaurant_list, restaurant_detail

urlpatterns = [
    path('', index, name="index"),
]

urlpatterns += [
    path('user/', include('django.contrib.auth.urls')),
    path('user/profile/', user_profile, name="profile"),
    path('user/signup/', user_signup, name="signup"),
    #path('user/addtowishlist/', addwish, name="addwish"),
    #path('user/addtowishlist/<uuid:rid>/', addwish)
]

urlpatterns += [
    path('restaurants/', restaurant_list, name="restaurantlist"),
    path('restaurants/<uuid:rid>/', restaurant_detail, name="restaurantdetail"),
]
