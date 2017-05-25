from django.conf.urls import url
from .views import index, dashboard, login, signup, logout

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^login/$', login, name="login"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^logout/$', logout, name="logout"),
]