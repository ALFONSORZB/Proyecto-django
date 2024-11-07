from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',views.sigin, name='sigin'),
    path('regis',views.regis, name='regis'),
    path('salir',views.salir, name='salir'),
    #path('sigin',views.sigin, name='sigin'),
    path('inicio',views.inicio, name='inicio'),
    path('compra',views.compra, name='comprar'),
    path('cliente',views.cliente, name='cliente'),
    path('elimiar/<int:id>',views.eliminar, name='eliminar'),
    path('vcliente',views.vcliente, name='vcliente'),
    path('actualizar/<int:id>',views.actualizar, name='actualizar'),
    path('vproducto',views.vproducto, name='vproducto'),
    path('rtenis',views.rtenis, name='rtenis'),
    path('elimiarp/<int:id>',views.eliminarp, name='eliminarp'),
    path('actualizarp/<int:id>',views.actualizarp, name='actualizarp')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)