from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Post


class PostCreate(CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ['image', 'title', 'text']

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect(self.get_success_url())


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        comments = self.object.comments.order_by('-created_at')
        paginator = Paginator(comments, 2)
        page = self.request.GET.get('page')

        try:
            comments = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            comments = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            comments = paginator.page(paginator.num_pages)
        context['comments'] = comments
        return context


class PostList(ListView):
    model = Post
    template_name = 'posts/list.html'
    paginate_by = 5

    def get_queryset(self):
        query = {k: v for k, v in self.request.GET.items() if k != 'page'}
        if not query:
            return Post.objects.order_by('-created_at')
        else:
            queryset = Post.objects.filter(
                Q(user__email__icontains=query.get('kw')) |
                Q(title__icontains=query.get('kw')) |
                Q(text__icontains=query.get('kw')),
                user__country__icontains=query.get('country'),
                user__city__icontains=query.get('city')
            )
            return queryset
