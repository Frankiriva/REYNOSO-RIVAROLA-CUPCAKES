from flask import Flask,render_template, request, redirect
from conexion import DB
from claseCliente import Cliente
from claseMenu import MenuComida
from claseEmpleado import Empleado
from claseSucursal import Sucursal

DB().SetConection('127.0.0.1', 'root', 'alumno', 'mydb')

conexion=DB()
menu=MenuComida()
unEmpleado=Empleado()
UnitaSucursal=Sucursal()
Unaqueja=Queja()

app = Flask(__name__)


@app.route("/Quejas",methods=["GET","POST"])
def quejitas():
    lista=[]
    Seleccionar_Sucursal = DB().run("SELECT * FROM Sucursal;")
    for item in Seleccionar_Sucursal:
            UnaQueja=UnaQueja()
            UnaQueja.deserealizar(item)
            lista.append(UnaQueja)
    return render_template("Quejas.html",lista=lista)

def deserealizar(self):
    self.idSucursal= DiccionarioSucursal["idSucursal"]
    self.NombreSucursal= DiccionarioSucursal["NombreSucursal"]
    self.DireccionSucursal= DiccionarioSucursal["DireccionSucursal"]


#HACER DESPLAZABLE DE SUCURSALES


if __name__ == "__main__":
    app.run(debug=True)