from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',article_views.articles_list,name='home'),
    url(r'^articles/',include('articles.urls')),
    url(r'^accounts/',include('Accounts.urls')),
    url(r'^about/$', views.about),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)