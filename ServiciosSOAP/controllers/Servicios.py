# -*- coding: utf-8 -*-
from gluon.tools import Service
service = Service(globals())

@service.soap('AddIntegers',returns={'AddResult':int},args={'a':int, 'b':int})
def add(a,b):
    return a+b

@service.soap('SubIntegers',returns={'SubResult':int},args={'a':int, 'b':int})
def sub(a,b):
    return a-b

def call():
    return service()
