from django.urls import path
from .views import *

app_name = 'desktop'

urlpatterns = [

    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/login', DTLoginView.as_view(), name='login'),
    path('accounts/logout', DTLogoutView.as_view(), name='logout'),
    path('', index, name='index'),

]
