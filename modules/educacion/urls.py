from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<pk>[0-9]+)/$',contenido, name="contenido"),
    url(r'^categoria/(?P<pk>[a-zA-Z]+)/$', contenido_categoria, name="contenido_categoria"),
    url(r'^busqueda/$', contenido_busqueda, name="contenido_busqueda"),
    url(r'^cursos/$', cursos, name="cursos"),
    url(r'^cursos/(?P<pk>[0-9]+)/$', cursos_ver, name="cursos"),
    url(r'^cursos/agregar/$', cursos_agregar, name="cursos_agregar"),
    url(r'^cursos/agregar/(?P<pk>[0-9]+)/$', cursos_registrar, name="curso_registrar"),
    url(r'^cursos/eliminar/(?P<pk>[0-9]+)/$', cursos_eliminar, name="curso_eliminar"),
]