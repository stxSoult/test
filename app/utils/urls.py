from django.conf.urls import url
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.utils.views import Votes, Comments
from app.utils.models import LikeDislike
from app.posts.models import Post

urlpatterns = [
    # likes / dislikes
    url(r'^like/post/(?P<pk>\d+)/$',
        login_required(Votes.as_view(model=Post, vote_type=LikeDislike.LIKE)),
        name='post-like'),

    url(r'^like/dislike/(?P<pk>\d+)/$',
        login_required(Votes.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
        name='post-dislike'),


    # comments
    url(r'^comment/post/(?P<pk>\d+)/$',
        login_required(Comments.as_view(model=Post)),
        name='post-comment'),
]
