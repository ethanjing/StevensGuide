from django.urls import path
from django.conf.urls import include
from .views import index, user_signup, user_profile, restaurant_list, restaurant_detail

urlpatterns = [
    path('', index, name="index"),
]

urlpatterns += [
    path('user/', include('django.contrib.auth.urls')),
    #path('user/login/', user_login, name="login"),
    #path('user/logout/', user_logout, name="logout"),
    path('user/profile/', user_profile, name="profile"),
    path('user/signup/', user_signup, name="signup"),
]

urlpatterns += [
    path('restaurants/', restaurant_list),
    path('restaurants/<uuid:rid>/', restaurant_detail)
]
