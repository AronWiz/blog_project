from django.urls import path, include, re_path
from blog import views

urlpatterns = [
    re_path('^$', views.PostListView.as_view(),name='post_list'),
    re_path('^about/$', views.AboutView.as_view(),name='about'),
    re_path('^post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
    re_path('^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    re_path('^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    re_path('^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(),name='post_remove'),
    re_path('^drafts/$', views.DraftListView.as_view(),name='post_draft_list'),
]
