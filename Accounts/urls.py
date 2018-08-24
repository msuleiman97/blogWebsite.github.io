from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views 

app_name= 'accounts'

urlpatterns=[
    url(r'^signup/$',views.signup_view, name="signup"),
    url(r'^login/$',views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^profile/$', views.profile, name="porfile"),
    url(r'^profile/edit/$', views.edit_profile, name='edit-porfile'),
    url(r'^friends/$', views.friends, name="friends"),
    #url(r'^profile/edit/$', views.edit_profile, name="edit-porfile"),
    url(r'^profile/change-password/$', views.change_password, name="change-password"),
    url(r'^reset-password/$', auth_views.password_reset, name="reset_password"),
    url('^reset-password/done/$',auth_views.password_reset_done, name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)=(?P<token>.+)/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', auth_views.password_reset_complete, name="password_reset_complete")
    
]
