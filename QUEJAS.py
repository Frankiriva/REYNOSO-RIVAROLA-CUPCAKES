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

dictSucursal = conexion.run("SELECT * FROM Sucursal")

listaSucursal = []

for item in dictSucursal:
    objSucursal = Sucursal()
    objSucursal.getSucursal(item["idSucursal"])
    listaSucursal.append(objSucursal)


class Quejitas(object):
    idSucursal = None
    NombreSucursal = None
    DireccionSucursal = None

    def deserealizar(self, DiccionarioSucursal):
        self.idSucursal = DiccionarioSucursal["idSucursal"]
        self.NombreSucursal = DiccionarioSucursal["NombreSucursal"]
        self.DireccionSucursal = DiccionarioSucursal["DireccionSucursal"]




app = Flask(__name__)


@app.route("/Quejas",methods=["GET","POST"])
def AgregarQueja():
    queja = request.form.get("queja")
    menu = request.form.get("menu")
    sucursal=request.form.get("sucursal")

    DB.run("INSERT INTO Clientes VALUES (NULL,'"+queja+"','"+menu+"','"+sucursal+"');")

    return render_template("Quejas.html",lista=listaSucursal)


if __name__ == "__main__":
    app.run(debug=True)

