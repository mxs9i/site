from django.urls import include, path, re_path
from .views import *
from django.views.decorators.cache import cache_page
# Здесь объявляем пути, а так же объеявляем функции куда переходим (функции лежат во views.py)

urlpatterns = [
    path('', cache_page(15*60)(index), name='home'),
    path('jims', cache_page(15*60)(halls), name='halls'),
    path('abonements', (abonements), name='abonements'),
    path('ourcomand', cache_page(15*60)(ourcomand), name='ourcomand'),
    path('mypage', (mypage), name='mypage'),
    path('loveJim', loveJim, name = 'loveJim'),
    path('createtrening', (createtrening), name='createtrening'),
    path('paty/<int:pk>/updateTrening', TreningUpdate.as_view(), name='updateTrening'),
    path('paty/<int:pk>/deleteTrening', TreningDelete.as_view(), name='deleteTrening'),
    path('signIn', cache_page(15*60)(LoginUser.as_view()), name='signIn'),
    path('signUp', cache_page(60)(RegisterUser.as_view()), name='signUp'),
    path('lovingJimJson.json', lovingJimJson, name = 'lovingJimJson'),
    path('deletecookie/', delete_coockie, name='deletecoockie'),
    path('logout', logout_user, name='logout'),
]