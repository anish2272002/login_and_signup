from django.urls import path
from .views import index,logout_user,signup_user,login_user,create

from django.conf import settings
from django.conf.urls.static import static

app_name='app'

urlpatterns = [
    path('',index,name='index'),
    path('sign',signup_user,name="sign"),
    path('login',login_user,name="login"),
    path('logout',logout_user,name="logout"),
    path('create',create,name="create"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)