from django.conf.urls import url
from . import views
from . import openPdf

urlpatterns = [
    # Filtros...
    url(r'^recargaDepa/$', views.recargaDepa),
    url(r'^recargaProv/(\d+)/(\d+)/$', views.recargaProv),
    url(r'^recargaDis/(\d+)/(\d+)/(\d+)/$', views.recargaDis),
    url(r'^recargaZona/(\d+)/$', views.recargaZona),

    # Segmentacion...
    url(r'^segrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.segrecargaTabla01),
    
    # Croquis...
    url(r'^crorecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla01),
    url(r'^crorecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla02),
    url(r'^descargarPdf/(\d+)/(\d+)/(\d+)/(\d+)/$', openPdf.descargarPdf),

    # Croquis tabular...
    url(r'^crotabrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crotabrecargaTabla01),
    url(r'^crotabrecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crotabrecargaTabla02),
    url(r'^descargarPdftab/(\d+)/(\d+)/(\d+)/(\d+)/$', openPdf.descargarPdftab),

    # Legajo...
    url(r'^legajorecargaTabla/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.legajorecargaTabla),
    url(r'^generarEtiqueta/(\d+)/$', views.generarEtiqueta),

    # Calidad...
    url(r'^calidadrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.calidadrecargaTabla01),
    url(r'^calidadrecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.calidadrecargaTabla02),
    url(r'^calidadguardarObs/(\d+)/(\d+)/(\d+)/(\w+)/$', views.calidadguardarObs),

    # Reportes...    
    url(r'^tablaReporte/(\d+)/(\d+)/$', views.tablaReporte),

    # Reportes...    
    url(r'^tablaReportetabular/(\d+)/(\d+)/$', views.tablaReportetabular),    
]
