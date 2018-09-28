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

@app.route("/inicio", methods=["GET"])
def Inicio():
    return render_template("Inicio.html")

@app.route("/Empleados", methods=["GET"])
def empleados():
    return render_template("Empleados.html")

@app.route("/Clientes", methods=["GET"])
def clientes():
    return render_template("Clientes.html")

@app.route("/Menu", methods=["GET"])
def menu():
    return render_template("Menu.html")

@app.route("/Sucursales", methods=["GET"])
def sucursales():
    return render_template("Sucursales.html")

@app.route("/AgregarEmpleado", methods=["GET"])
def agregarempleados():
    return render_template("Agregar_Empleado.html")

@app.route("/CompletarAgregarEmpleado", methods=["POST", "GET"])
def completaragregarempleado():
    nombre= request.form.get("nombre")
    apellido= request.form.get("apellido")
    dni = request.form.get("dni")
    sucursal = request.form.get("sucursal")
    unEmpleado = Empleado()
    unitaSucursal = Sucursal()
    unitaSucursal.getSucursal(sucursal)
    unEmpleado.AgregarEmpleado(nombre,apellido,dni,sucursal)

    return redirect("/AgregarEmpleado")

@app.route("/CompletarAgregarCliente", methods=["POST", "GET"])
def completaragregarcliente():
    queja=request.form.get("queja")
    pedido=request.form.get("pedido")
    sucursal=request.form.get("sucursal")
    unCliente = Cliente()
    unitaSucursal = Sucursal()
    unitaSucursal.getSucursal(sucursal)
    unCliente.AgregarCliente(queja,pedido,sucursal)

    return redirect("/AgregarCliente")

@app.route("/CompletarAgregarMenu", methods=["POST", "GET"])
def completaragregarmenu():
    nombre=request.form.get("nombre")
    precio=request.form.get("precio")
    tipo=request.form.get("tipo")
    sucursal=request.form.get("sucursal")
    unMenu = MenuComida()
    unitaSucursal = Sucursal()
    unitaSucursal.getSucursal(sucursal)
    unMenu.AgregarMenu(nombre,precio,tipo,sucursal)

    return redirect("/AgregarMenu")

@app.route("/CompletarAgregarSucursal", methods=["POST", "GET"])
def completaragregarsucursal():
    nombre=request.form.get("nombre")
    direccion=request.form.get("direccion")
    unitaSucursal = Sucursal()
    unitaSucursal.AgregarSucursal(nombre, direccion)

    return redirect("/AgregarSucursal")

@app.route("/CompletarBorrarCliente", methods=["POST", "GET"])
def completarborrarcliente():
    id=request.form.get("id")
    unCliente = Cliente()
    unCliente.BorrarCliente(id)

    return redirect("/BorrarCliente")

@app.route("/CompletarBorrarEmpleado", methods=["POST","GET"])
def completarborrarempleado():
    id=request.form.get("id")
    unEmpleado = Empleado()
    unEmpleado.BorrarEmpleado(id)

    return redirect("/BorrarEmpleados")

@app.route("/CompletarBorrarSucursal", methods=["POST","GET"])
def completarborrarsucursal():
    id=request.form.get("id")
    UnitaSucursal = Sucursal()
    UnitaSucursal.BorrarSucursal(id)

    return redirect("/BorrarSucursal")

@app.route("/CompletarBorrarMenu",methods=["POST","GET"])
def completarborrarmenu():
    id=request.form.get("id")
    unMenu = MenuComida()
    unMenu.BorrarMenu(id)

    return redirect("/BorrarMenu")

@app.route("/CompletarModificarCliente",methods=["POST","GET"])
def completarmodificarcliente():
    queja=request.form.get("queja")
    pedido=request.form.get("pedido")
    id=request.form.get("id")
    unCliente = Cliente()
    unitaSucursal = Sucursal()
    unitaSucursal.getSucursal()
    unCliente.UpdateCliente(queja, pedido, id)

    return redirect("/ModificarCliente")

@app.route("/ModificarEmpleados", methods=["GET"])
def modificarempleados():
    return render_template("Modificar_Empleado.html")

@app.route("/BorrarEmpleados", methods=["GET"])
def borrarempleados():
    return render_template("Borrar_Empleado.html")

@app.route("/AgregarCliente", methods=["GET"])
def agregarcliente():
    return render_template("Agregar_Cliente.html")

@app.route("/BorrarCliente", methods=["GET"])
def borrarcliente():
    return render_template("Borrar_Cliente.html")

@app.route("/ModificarCliente", methods=["GET"])
def modificarcliente():
    return render_template("Modificar_Cliente.html")

@app.route("/AgregarMenu", methods=["GET"])
def agregarmenu():
    return render_template("Agregar_Menu.html")

@app.route("/BorrarMenu", methods=["GET"])
def borrarmenu():
    return render_template("Borrar_Menu.html")

@app.route("/ModificarMenu", methods=["GET"])
def modificarmenu():
    return render_template("Modificar_Menu.html")

@app.route("/AgregarSucursal", methods=["GET","POST"])
def agregarsucursal():
    return render_template("Agregar_Sucursal.html")

@app.route("/BorrarSucursal", methods=["GET"])
def borrarsucursal():
    return render_template("Borrar_Sucursal.html")

@app.route("/ModificarSucursal", methods=["GET"])
def modificarsucursal():
    return render_template("Modificar_Sucursal.html")


if __name__ == "__main__":
    app.run(debug=True)

