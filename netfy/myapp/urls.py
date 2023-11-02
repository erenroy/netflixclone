from django.contrib import admin
from django.urls import path,include
from myapp import views

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('home/',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.login,name='login'),
    path('userlogout',views.userlogout,name='userlogout'),

    path('part1/',views.part1,name='part1'),
    path('part2/',views.part2,name='part2'),

    path('moviepage',views.moviepage,name='moviepage'),
    path('fmovie',views.fmovie,name='fmovie'),
    path('allmovie/<slug:post_slug>',views.allmovie,name='allmovie'),
    path('moviedetails/<slug:post_slug>',views.moviedetails,name='moviedetails'),

    path('moviepageshow',views.moviepageshow,name='moviepageshow'),
    path('searchpage',views.searchpage,name='searchpage'),
   # path('searchpage/<slug:query>/',views.searchpage,name='searchpage'),

    path('addtomylist/',views.addtomylist,name='addtomylist'),
    path('mylist/',views.mylist,name='mylist'),
    path('remove_mylist/',views.remove_mylist,name='remove_mylist'),


    path('aisearch',views.aisearch,name='aisearch'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
