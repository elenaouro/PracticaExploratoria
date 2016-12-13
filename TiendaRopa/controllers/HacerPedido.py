# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:58:54 2016

@author: elena
"""

from gluon.contrib.pysimplesoap.client import SoapClient


def HacerPedido():
    ID = request.vars.ID
    Fecha = request.vars.Fecha
    cantidad = request.vars.cantidad
    DNI = request.vars.DNI
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.HacerPedido(ID,Fecha,DNI,cantidad)
    return str(result['Status'])
    
def index():
    """
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.HacerPedido(1,20161213,12345678,2)
    return str(result['Status'])
    """
    form1 = FORM(TABLE(TR('DNI:',
              INPUT(_name='DNI', requires=IS_NOT_EMPTY())),
 TR('Fecha:', INPUT(_name='Fecha', requires=IS_NOT_EMPTY())),
 TR('ID producto: ', INPUT(_name='ID', requires=IS_NOT_EMPTY())),
 TR('Cantidad: ', INPUT(_name='cantidad', requires=IS_NOT_EMPTY())),
INPUT(_type='submit', _value='Hacer pedido')))
    if form1.process(formname='form_one').accepted:
        redirect(URL('HacerPedido',vars=dict(ID=request.vars.ID,Fecha=request.vars.Fecha,DNI=request.vars.DNI,cantidad=request.vars.cantidad)))

    return form1
