from django.urls import path, include
from . import views

app_name = "api"

urlpatterns = [
    path(
        "author/",
        views.AuthorModelViewSet.as_view(
            {
                'get': 'list',
                'post':'create'
            }
        ),
        name="author-list",
    ),
    path(
        "author/<int:pk>/",
        views.AuthorModelViewSet.as_view(
            {
                'get': 'retrieve',
                'patch':'partial_update',
                'delete':'destroy'
            }
        ),
        name="author-list",
    ),
    path(
        "author/restrict/",
        views.AuthorRestrictModelViewSet.as_view(
            {
                'get': 'list',
            }
        ),
        name="author-restrict",
    ),

]
