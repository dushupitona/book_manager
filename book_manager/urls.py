"""
URL configuration for book_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from main_page.views import IndexView, book_detail, AddBookView, del_book


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:book_id>/', book_detail, name='book_go'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('<int:book_id>/delete/', del_book, name='del_book'),    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)