# -*- coding: utf-8 -*-

from gluon.contrib.pysimplesoap.client import SoapClient

def ConsultarProductos():
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.ConsultaProductos()
    return str(result[Productos])
    
def index():
    """
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.HacerPedido(1,20161213,12345678,2)
    return str(result['Status'])
    """
    form1 = FORM(INPUT(_value='Consultar productos', _type='submit'))
    if form1.process(formname='form_one').accepted:
        redirect(URL('ConsultarProductos'))
    return form1