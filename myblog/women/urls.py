from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', WomenIndex.as_view(), name='home'),
    path('about/', GetAbout.as_view(), name='about'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUserForm.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('cat/<slug:cat_slug>', ShowCategory.as_view(), name='cat'),
    path('tag/<slug:tag_slug>', ShowTags.as_view(), name='tag'),
]