from django.urls import path

from apps.pages.views import view_post

app_name = 'pages'

urlpatterns = [
    path('',view_post,name='view_post'),
]