from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create-post/$', views.CreatePost.as_view(), name="create-post"),
    url(r'^register/$', views.RegisterUser.as_view(), name="register"),
    # url(r'^search/(?P<name>[])/$')
]
