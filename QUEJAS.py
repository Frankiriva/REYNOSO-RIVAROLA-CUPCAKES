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

app = Flask(__name__)

@app.route("/Quejas",methods=["GET"])
def quejitas():
    return render_template("Quejas.html")

Grab= DB.run("select * from sucursales")

listasucursales=[]

for item in Grab:








if __name__ == "__main__":
    app.run(debug=True)