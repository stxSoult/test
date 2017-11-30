from django.conf.urls import url
from django.contrib.auth.views import login, logout

from app.accounts import views

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^logout/$', logout,
        {'next_page': '/login'}, name='logout'),

    url(r'^register/$', views.CustomRegisterView.as_view(), name='register'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.EmailConfirmation.as_view(),
        name='activate'),
]