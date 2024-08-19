from django.urls import path
from app import views

urlpatterns = [
  path('contact/', views.contact_view, name='contact'),
  path('thanks/', views.thanks_view, name='thanks'),
  path('login/', views.login_view, name='login'),
  path('member/', views.member_view, name='member'),
  path('list_member/', views.member_list, name='member_list'),
]

