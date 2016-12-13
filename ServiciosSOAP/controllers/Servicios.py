# -*- coding: utf-8 -*-
import sqlite3 as sqlite
from gluon.tools import Service
import numpy as np

service = Service(globals())


@service.soap('HacerPedido',returns={'Status':str}, args={'producto':int,'fecha':int,'dni':int,'cantidad':int})
def hacer_pedido(producto,fecha,dni,cantidad):
    try:
        precio_total=0
        con = None
        con = sqlite.connect('/home/elena/Documents/web2py/applications/ServiciosSOAP/databases/tiendaBD')
        cur = con.cursor()
        cur.execute("SELECT cantidad FROM productos WHERE id="+str(producto))
        results = cur.fetchall()
        cantidadAntigua=results[0][0]
        if(cantidadAntigua<cantidad): return "Error: cantidad no disponible"
        cur.execute("SELECT precio FROM productos where id="+str(producto)) 
        results = cur.fetchall()
        precio_total=cantidad*int(results[0][0])
        cur.execute("SELECT MAX(id) AS maxim FROM pedidos")
        results = cur.fetchall()
        id_pedido=int(results[0][0])+1
        cur.execute("INSERT INTO pedidos VALUES ("+str(id_pedido)+","+str(dni)+","+str(fecha)+","+str(precio_total)+")")
        cur.execute("INSERT INTO producto_pedido  VALUES("+str(producto)+","+str(id_pedido)+","+str(cantidad)+")")     
        cur.execute("UPDATE productos SET cantidad="+str(cantidadAntigua-cantidad)+" WHERE id="+str(producto))
    except sqlite.Error as er:
        return str(er)    
    finally:
        if con:
            con.commit()
            con.close()
    return "Se ha realizado el pedido correctamente"
    
#Consulta
@service.soap('ConsultaProductos',returns={'Productos':str}, args={})
def consulta_productos():
    ListaProductos = "Error"
    try:
        con = None
        con = sqlite.connect('/home/elena/Documents/web2py/applications/ServiciosSOAP/databases/tiendaBD')
        cur = con.cursor()
        cur.execute("SELECT * FROM productos")
        ListaProductos = ""
        results = cur.fetchall()
        for tupla in results:
            ListaProductos += "Numero de referencia:"+str(tupla[0])+" Nombre: "+tupla[1]+" Precio: "+str(tupla[2])+" Cantidad: "+str(tupla[3])+" Descripcion: "+str(tupla[4])+"<br>"
    finally:
        if con:
            con.close()
    return ListaProductos
    
@service.soap('InformacionProducto',returns={'Producto':str}, args={'ID':int})
def informacion_producto(ID):
    Producto = "Error"
    try:
        con = None
        con = sqlite.connect('/home/elena/Documents/web2py/applications/ServiciosSOAP/databases/tiendaBD')
        cur = con.cursor()
        cur.execute("SELECT * FROM productos WHERE id="+str(ID))
        Producto = ""
        results = cur.fetchall()
        for tupla in results:
            Producto += "Numero de referencia: "+str(tupla[0])+" Nombre: "+tupla[1]+" Precio: "+str(tupla[2])+" Cantidad:"+str(tupla[3])+" Descripcion:"+str(tupla[4])+"<br>"
    finally:
        if con:
            con.close()
    return Producto

@service.soap('ConsultarPedidos',returns={'Pedidos':str}, args={'dni':int})
def consultar_pedidos(dni):
    pedidos = "Error"
    try:
        con = None
        con = sqlite.connect('/home/elena/Documents/web2py/applications/ServiciosSOAP/databases/tiendaBD')
        cur = con.cursor()
        cur.execute("SELECT * FROM pedidos p, producto_pedido pp, productos pr WHERE p.dni_cliente="+str(dni)+" AND p.id=pp.id_pedido AND pp.id_producto=pr.id")   
        pedidos = ""
        results = cur.fetchall()
        id_pedido = 0
        for tupla in results:
            if(tupla[0]!=id_pedido):
                id_pedido=tupla[0]
                pedidos += "<br> Numero de pedido: "+str(tupla[0])+" Fecha: "+str(tupla[2])+" precio total: "+str(tupla[3])+"<br>"
            pedidos += "Numero de referencia: "+str(tupla[7])+" Producto: "+tupla[8]+" Precio: "+str(tupla[9])+" Cantidad: "+str(tupla[6])+"<br>"
    finally:
        if con:
            con.close()
    return pedidos

        
def call():
    return service()
