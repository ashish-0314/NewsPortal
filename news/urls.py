from django.urls import path
from . import views

urlpatterns = [
    path(
        'article/<int:id>/publish/',
        views.publishArticle,
        name='publish_article'
    ),
]