# -*- coding: utf-8 -*-
from gluon.contrib.pysimplesoap.client import SoapClient

def ConsultarPedidos():
    dni = request.vars.dni
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.ConsultarPedidos(dni)
    return str(result['Pedidos'])
    
def index():
    """
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.HacerPedido(1,20161213,12345678,2)
    return str(result['Status'])
    """
    form1 = FORM('DNI:',
              INPUT(_name='DNI', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit', _value='Consultar pedidos'))
    if form1.process(formname='form_one').accepted:
        redirect(URL('ConsultarPedidos',vars=dict(dni=request.vars.DNI)))

    return form1