# -*- coding: utf-8 -*-

from gluon.contrib.pysimplesoap.client import SoapClient

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    client = SoapClient(wsdl="http://localhost:8000/ServiciosSOAP/Servicios/call/soap?WSDL")
    result = client.AddIntegers(a=1, b=2)
    return str(result['AddResult'])
    
