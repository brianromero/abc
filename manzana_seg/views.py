from django.http import HttpResponse
from .models import Departamento, Provincia, Distrito, Zona
import json
from django.db.models import Count

# Croquis y listado...
import os
import zipfile
import StringIO

from urllib2 import Request, urlopen
from pyPdf import PdfFileWriter, PdfFileReader

# Legajos...
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.graphics.barcode import code39

# Filtros...
def recargaDepa(request):
    dataAux = dataDepa()
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataDepa():    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaDepa %s,%s,%s,%s,%s', ('0','0','0','0','0') )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def recargaProv(request, depa, prov):
    dataAux = dataProv(depa,prov)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataProv(depa, prov):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaProv %s,%s,%s,%s,%s', (0,depa,prov,0,0) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def recargaDis(request, depa, prov, dis):
    dataAux = dataDis(depa,prov,dis)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataDis(depa, prov, dis):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaDis %s,%s,%s,%s,%s', (0,depa,prov,dis,0) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def recargaZona(request, ubigeo):
    dataAux = dataZona(ubigeo)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataZona(ubigeo):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaZona %s,%s', (ubigeo,0) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

# Segmentacion...
def segrecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataSeg(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataSeg(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTablaSeg %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

# Croquis y listado...
def crorecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCro(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCro(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTablaCro %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu    

def crorecargaTabla02(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCroquis(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCroquis(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaPopCroquis %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

# Croquis y listado tabular...
def crotabrecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCroTab(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCroTab(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTablaCroTab %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu    

def crotabrecargaTabla02(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCroquisTab(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCroquisTab(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaPopCroquisTab %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

# Legajo...
def legajorecargaTabla(request, tipo, ccdd, ccpp, ccdi, zona, distri):
    dataAux = dataLegajo(tipo, ccdd, ccpp, ccdi, zona, distri)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataLegajo(tipo, ccdd, ccpp, ccdi, zona, distri):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaLegajo %s,%s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona,distri) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def generarEtiqueta(request, ubigeo):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename="+ubigeo+".pdf"
    buff = BytesIO()
    doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=70, leftMargin=70, topMargin=60, bottomMargin=18,)
    story = []
    string = ubigeo
    st = code39.Extended39(string)
    story.append(st)        
    doc.build(story)
    response.write(buff.getvalue())
    buff.close()
    return response

# Reporte...
def tablaReporte(request, tipo,ubigeo):
    dataAux = dataReporte(tipo, ubigeo)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataReporte(tipo,ubigeo):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaReporte %s,%s', (tipo,ubigeo) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu  

# Reporte tabular...
def tablaReportetabular(request, tipo,ubigeo):
    dataAux = dataReportetabular(tipo, ubigeo)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataReportetabular(tipo,ubigeo):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaReporte %s,%s', (tipo,ubigeo) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu  

# Calidad...
def calidadrecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCont(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCont(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTablaCont %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def calidadrecargaTabla02(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCalidad01(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCalidad01(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaPopCont %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def calidadguardarObs(request, ubigeo, zona, aeu, obs):
    dataAux = guardarCalidad01(ubigeo, zona, aeu, obs)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def guardarCalidad01(ubigeo, zona, aeu, obs):    
    from django.db import connection
    cursor = connection.cursor()
    print ubigeo
    print zona
    print aeu
    print obs
    cursor.execute('exec GuardarObserCont %s,%s,%s,%s', (ubigeo,zona,aeu,obs) )    
    #columns = [column[0] for column in cursor.description]
    #print columns
    menu = []
    #for row in cursor.fetchall():
    #    menu.append(dict(zip(columns, row)))
    return menu
