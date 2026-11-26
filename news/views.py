from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Article


@login_required
@require_POST
def publishArticle(request, id):

    # Check custom permission
    if not request.user.has_perm('news.can_publish'):

        return JsonResponse({
            'error': 'You do not have permission to publish articles'
        }, status=403)

    # Get article
    article = get_object_or_404(Article, id=id)

    # Publish article
    article.published = True
    article.save()

    return JsonResponse({
        'message': 'Article published successfully',
        'headline': article.headline,
        'published': article.published
    })