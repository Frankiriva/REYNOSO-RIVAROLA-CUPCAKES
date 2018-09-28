from conexion import DB
from claseSucursal import Sucursal

class Empleado(object):
    idEmpleado= None
    NombreEmpleado= None
    ApellidoEmpleado= None
    DNI_Empleado= None
    Sucursal=None

    def AgregarEmpleado(self,Nombre,Apellido,DNI,Sucursal):
        self.NombreEmpleado=Nombre
        self.ApellidoEmpleado=Apellido
        self.DNI_Empleado=DNI
        self.Sucursal=Sucursal

        DB().run("INSERT INTO Empleados VALUES (NULL, '"+self.NombreEmpleado+"','"+self.ApellidoEmpleado+"','"+self.DNI_Empleado+"','"+str(self.Sucursal)+"');")


    def BorrarEmpleado(self,idEmpleado):

        DB().run("DELETE FROM Empleados WHERE idEmpleado="+idEmpleado+";")

    def UpdateEmpleado(self,Nombre,Apellido,DNI,id):

        DB().run("UPDATE Empleados SET NombreEmpleado= '"+Nombre+"',ApellidoEmpleado='"+Apellido+ "',DNI_Empleado= '"+DNI+"' WHERE idEmpleado= '"+str(id)+"';")

    def DeserializarEmpleado(self,DiccionarioEmpleado):
        self.idEmpleado=DiccionarioEmpleado["idEmpleado"]
        self.NombreEmpleado=DiccionarioEmpleado["NombreEmpleado"]
        self.ApellidoEmpleado=DiccionarioEmpleado["ApellidoEmpleado"]
        self.DNI_Empleado=DiccionarioEmpleado["DNI_Empleado"]
        self.Sucursal=DiccionarioEmpleado["Sucursal"]