# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:58:53 2016

@author: elena
"""
from gluon.contrib.pysimplesoap.client import SoapClient

def InfoProducto():
    ID = request.vars.ID
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.InformacionProducto(ID)
    return str(result['Producto'])
    
def index():
    """
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.HacerPedido(1,20161213,12345678,2)
    return str(result['Status'])
    """
    form1 = FORM('ID del producto:',
              INPUT(_name='ID', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit', _value='Consultar informacion producto'))
    if form1.process(formname='form_one').accepted:
        redirect(URL('InfoProducto',vars=dict(ID=request.vars.ID)))

    return form1
