from django.conf.urls import url
from app.posts import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^create/$', views.PostCreate.as_view(), name='post-create')
]