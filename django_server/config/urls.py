from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', TemplateView.as_view(template_name='main.html'),name='main'),  # 메인 페이지 URL
   path('', include('app.urls')),  # contact 앱의 urls 포함, 심어주는 작업이다.
]




