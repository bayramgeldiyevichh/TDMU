from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sub_category/<int:id>/', views.sub_category, name="sub_category"),
    path('soraglar/<int:id>/', views.soraglar, name='soraglar'),
    path('profile_register/', views.profile_register, name='profile_register'),
    path('profile_setting/', views.profile_setting, name='profile_setting'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('statistika/', views.statistika, name="statistika"),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='logout'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sub_cat_percent/<int:id>/', views.sub_cat_percent, name="sub_cat_percent"),
    # path('statistika/<int:id>/', views.statistika, name='statistiaka')
]