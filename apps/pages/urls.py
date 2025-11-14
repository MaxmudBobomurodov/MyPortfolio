from django.urls import path

from apps.pages.views import ViewPost

app_name = 'pages'

urlpatterns = [
    path('',ViewPost.as_view(),name='view_post'),
]