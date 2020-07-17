from django.urls import path

from .views import index, blog, selected_post

app_name = 'post'
urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog/<str:post_slug>', selected_post, name='selected_post')

]
