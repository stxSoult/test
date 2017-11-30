from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike, Comment

# Create your views here.


class Votes(View):
    model = None
    vote_type = None

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        try:
            likedislike = LikeDislike.objects.get(
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id,
                user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
            else:
                likedislike.delete()
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)

        data = {
            'likes': obj.votes.likes().count(),
            'dislikes': obj.votes.dislikes().count(),
            'sum_rating': obj.votes.sum_rating()
        }

        return JsonResponse(data, content_type='application/json')


class Comments(View):
    model = None

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)

        if len(request.POST.get('text')) < 10:
            return JsonResponse({'error': 'Messages is to short'})
        comment = Comment.objects.create(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id,
            user=request.user,
            text=request.POST.get('text')
        )

        print(comment)
        return JsonResponse({'user': comment.user.email, 'text': comment.text})

    def get(self):
        return redirect('/')