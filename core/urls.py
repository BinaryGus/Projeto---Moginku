from django.contrib import admin
from django.urls import path, include
from core.views import blog_feed  
from . import views


urlpatterns = [
    path('', blog_feed, name='home'), 
    path('admin/', admin.site.urls), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', views.blog_feed, name='blog_feed'), 
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('games/', views.games, name='games'),
    path('games/<slug:slug>/', views.game_detail, name='game_detail'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

