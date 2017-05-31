from django.conf.urls import url
from .views import index, contenido, contenido_categoria, contenido_busqueda

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<pk>[0-9]+)/$',contenido, name="contenido"),
    url(r'^categoria/(?P<pk>[a-zA-Z]+)/$', contenido_categoria, name="contenido_categoria"),
    url(r'^busqueda/$', contenido_busqueda, name="contenido_busqueda"),
]