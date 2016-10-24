from django.http import HttpResponse
from urllib2 import Request, urlopen
from pyPdf import PdfFileWriter, PdfFileReader
from StringIO import StringIO
from .models import Departamento
from django.db.models import Count
import json
import zipfile
import os
import StringIO
import urllib2
from .models import Zona, TablaAeu 

#Croquis y listado...
def descargarPdf(request,ubigeo,zona,tipo,area):
    lista = []
    dataAux = dataZip(ubigeo,zona,tipo,area,0)
    areaAux = ""
    if area == '0':
        areaAux="urbano"
    else:
        areaAux="rural"    
    for pdf in dataAux:
        if tipo == '1':
            ruta = "http://192.168.221.123/desarrollo/cpv2017/segm_esp/"+areaAux+"/"+ubigeo+"/"+zona+"/"+ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+".pdf"
            nombrePdf = ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+".pdf"
            lista.append(nombrePdf)
            download_url=ruta
            response = urllib2.urlopen(download_url) 
            file = open(ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+".pdf", 'wb')
        if tipo == '2':
            ruta = "http://192.168.221.123/desarrollo/cpv2017/segm_esp/"+areaAux+"/"+ubigeo+"/"+zona+"/"+ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+str(pdf.get("AEU",None))+".pdf"
            nombrePdf = ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+str(pdf.get("AEU",None))+".pdf"
            lista.append(nombrePdf)
            download_url=ruta
            response = urllib2.urlopen(download_url)
            file = open(ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+str(pdf.get("AEU",None))+".pdf", 'wb')            
        file.write(response.read())
        file.close()
    s = descargarPdfAux(lista)
    resp = HttpResponse(s.getvalue(), content_type='application/zip')
    if tipo == '1':
        resp['Content-Disposition']='attachment; filename=seccion.zip'
    else:
        resp['Content-Disposition']='attachment; filename=aeu.zip'
    return resp

#Croquis y listado tabular...
def descargarPdftab(request,ubigeo,zona,tipo,area):
    lista = []
    dataAux = dataZip(ubigeo,zona,tipo,area,1)
    areaAux = ""
    if area == '0':
        areaAux="urbano"
    else:
        areaAux="rural"    
    for pdf in dataAux:
        if tipo == '1':
            ruta = "http://192.168.221.123/desarrollo/cpv2017/segm_tab/"+areaAux+"/"+ubigeo+"/"+zona+"/"+ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+".pdf"
            nombrePdf = ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+".pdf"
            lista.append(nombrePdf)
            download_url=ruta
            response = urllib2.urlopen(download_url)
            file = open(ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+".pdf", 'wb')
        if tipo == '2':            
            ruta = "http://192.168.221.123/desarrollo/cpv2017/segm_tab/"+areaAux+"/"+ubigeo+"/"+zona+"/"+ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+str(pdf.get("AEU",None))+".pdf"
            nombrePdf = ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+str(pdf.get("AEU",None))+".pdf"
            lista.append(nombrePdf)
            download_url=ruta
            response = urllib2.urlopen(download_url)
            file = open(ubigeo+zona+("00" + str(pdf.get("SECCION",None)))[-3:]+str(pdf.get("AEU",None))+".pdf", 'wb')            
        file.write(response.read())
        file.close()
    s = descargarPdfAux(lista)
    resp = HttpResponse(s.getvalue(), content_type='application/zip')
    if tipo == '1':
        resp['Content-Disposition']='attachment; filename=seccionTabular.zip'
    else:
        resp['Content-Disposition']='attachment; filename=aeuTabular.zip'
    return resp

#Metodos genericos...
def dataZip(ubigeo, zona, tipo, area, modulo):    
    from django.db import connection
    cursor = connection.cursor()
    if modulo == 0:
        cursor.execute('exec ListaZip %s,%s,%s,%s', (ubigeo,zona,tipo,area) )
    else:
        cursor.execute('exec ListaZipTab %s,%s,%s,%s', (ubigeo,zona,tipo,area) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def descargarPdfAux(lista):
    filenames_url = lista
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s,"w")
    for file_url in filenames_url:
        zf.write(file_url)          
    zf.close()
    return s
