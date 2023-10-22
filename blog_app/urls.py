from django.contrib import admin
from django.urls import path, include
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home_page'),
    path('detail/<int:id>/', views.detail, name='detailpage'),

    # path('contact_temp',views.contact, name='contact_page'),
    path('contact_us/', views.contact_us, name='contact'),

    path('create/', views.addtemp, name='addtemp'),
    path('add/', views.create, name='create'),


    path('delete/<int:id>/', views.delete, name='delete'),

    path('privacy/', views.privacy, name='privacy'),
    path('follow/', views.follow, name='follow'),

    path('comment', views.comment, name='comment')
    # path('add_comment/', views.add_comment, name= 'addcomm')

    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login')


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)