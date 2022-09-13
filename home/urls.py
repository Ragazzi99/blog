from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:theslug>', views.detail, name='detail'),
    path('postlike/', views.post_like, name='postlike'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('category/<str:id>/<slug:slug>', views.category, name='category'),
    path('search/', views.search, name='search'),
]
