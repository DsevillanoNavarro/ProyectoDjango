"""
URL configuration for proyectomustafa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from proyectomustafa import settings
from . import views
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', views.principal, name="principal"),
    path('animales/', Animales.as_view(), name="animales"),
    path('animales/<int:pk>', DetallesAnimales.as_view(), name="detalleAnimales"),
    path('noticias/', Noticias.as_view(), name="noticias"),
    path('noticias/<int:pk>', DetallesNoticias.as_view(), name="detalleNoticias"),
    # path('contacto/', views.contacto, name="contacto"),
    path('registro/', CrearRegistro.as_view(), name="crearRegistro"),
    # path('login/', views.login, name="login"),
    path('usuario/', UserMenuView.as_view(), name="usuario"),
    # path('usuario/animalesQueridos', views.animalesQueridos, name="animalesQueridos"),
    path('usuario/admin/crearAnimal', CrearAnimales.as_view(), name="crearAnimales"),
    path('usuario/admin/listarAnimales', ListarAnimales.as_view(), name="listarAnimales"),
    path('usuario/admin/editarAnimal/<int:pk>', EditarAnimales.as_view(), name="editarAnimal"),
    path('usuario/admin/borrarAnimal/<int:pk>', BorrarAnimales.as_view(), name="borrarAnimal"),
    path('usuario/admin/crearNoticia', CrearNoticias.as_view(), name="crearNoticias"),
    path('usuario/admin/listarNoticias', ListarNoticias.as_view(), name="listarNoticias"),
    path('usuario/admin/listarComentarios', ListarComentarios.as_view(), name="listarComentarios"),
    path('usuario/admin/editarComentarios/<int:pk>', EditarComentarios.as_view(), name="editarComentarios"),
    path('usuario/admin/borrarComentarios/<int:pk>', BorrarComentarios.as_view(), name="borrarComentarios"),
    path('usuario/admin/editarNoticia/<int:pk>', EditarNoticias.as_view(), name="editarNoticias"),
    path('usuario/admin/borrarNoticia/<int:pk>', BorrarNoticias.as_view(), name="borrarNoticias"),
    # path('usuario/admin/datosAnimales', views.datosAnimales, name="datosAnimales"),
    # path('usuario/admin/datosNoticias', views.datosNoticias, name="datosNoticias"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)