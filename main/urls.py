from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = 'main'

urlpatterns = [
    path('accounts/password/reset/', auth_views.PasswordResetView.as_view(
        template_name='main/password_reset_form.html',
        email_template_name='main/password_reset_email.html',
        success_url=reverse_lazy("main:password_reset_done")), name='password_reset'),
    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='main/password_reset_confirm.html',
             success_url=reverse_lazy("main:password_reset_complete")), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    #
    path('accounts/profile/delete', views.DeleteUserView.as_view(), name='delete_user'),
    path('accounts/register/activate/<str:sign>/', views.user_activate, name='register_activate'),
    path('accounts/register/done', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register', views.RegisterUserView.as_view(), name='register'),
    path('accounts/password/change/', views.BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/chnage?<int:pk>/', views.profile_bb_change, name='profile_bb_change'),
    path('accounts/profile/delete/<int:pk>/', views.profile_bb_delete, name='profile_bb_delete'),
    path('accounts/profile/add/', views.profile_bb_add, name='profile_bb_add'),
    path('accounts/profile/<int:pk>/', views.profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login', views.BBLoginView.as_view(), name='login'),
    path('<int:rubric_pk>/<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.by_rubric, name='by_rubric'),
    path('<str:page>/', views.other_page, name='other'),
    path('', views.index, name='index')
]