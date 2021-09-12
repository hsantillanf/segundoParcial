from datetime import date,datetime

class Empresa:
    def __init__(self,nom="Extermix",ruc="0999959844",telf="064684165",dir="nice to me too"): #parametros crear para que sea mas generico.
        self.nombre=nom
        self.ruc=ruc
        self.telefono=telf
        self.direccion=dir

    def mostrarEmpresa(self):
        print('Empresa:{:15} Ruc:{} Telefono:{} Direccion:{}'.format(self.nombre,self.ruc,self.telefono,self.direccion))

from abc import ABC,abstractclassmethod  
class Cliente(ABC):
    def __init__(self,nom,ced,telf,dir):
        self.nombre=nom
        self.cedula=ced
        self.telefono=telf
        self.direccion=dir

    @abstractclassmethod
    def getCedula(self):
        return self.cedula

    def mostrarCliente(self):
        print('Nombre:{:15} Cedula:{} Telefono:{} Direccion:{}'.format(self.nombre,self.cedula,self.telefono,self.direccion))

class ClienteCorporativo(Cliente):
    def __init__(self,nom,ced,telf,dir,contrato):
        super().__init__(nom,ced,telf,dir)
        self.__contrato = contrato

    @property #getter nos sirve para obetener el valor privado
    def contrato(self):
        return self.__contrato

    @contrato.setter #setter asigna un valor al atrivuto privado
    def contrato(self,value):
        if value:
            self.__contrato=value
        else:
            self.__contrato='Sin contrato'

    def mostrarCliente(self):
        print('Nombre:{:15} Contrato:{}'.format(self.nombre,self.__contrato))

class ClientePersonal(Cliente):
    def __init__(self,nom,ced,telf,dir,promocion=True):
        super().__init__(nom,ced,telf,dir)
        self.__promocion = promocion

    @property #getter nos sirve para obetener el valor privado
    def promocion(self):
        if self.__promocion == True:
            return "Usted tiene _15%_ de Descuento"
        else:
            return "No recibe ningun Descuento"

    def mostrarCliente(self):
        print('Nombre:{:15}'.format(self.nombre),self.__promocion)

    def getCedula(self):
        return super().getCedula()

class Articulo:
    secuencia=0
    iva=0.12
    def __init__(self,des,pre,sto):
        Articulo.secuencia += 1
        self.codigo=Articulo.secuencia
        self.descripcion=des
        self.precio=pre
        self.stock=sto

    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class Detalle_de_Venta:
    linea=0
    def __init__(self,articulo,cantidad):
        Detalle_de_Venta.linea += 1
        self.articulo=articulo
        self.cantidad=cantidad
        self.precio=articulo.precio
        self.cantidad=cantidad

class CabVenta:
    def __init__(self,empresa,factura,fecha,cliente,tot=0):
        self.empresa=empresa
        self.factura=factura
        self.fecha=fecha
        self.cliente=cliente
        self.total=tot
        self.detalleVent=[]

    def agregarDetalle(self,articulo,cantidad):
        detalle= Detalle_de_Venta(articulo,cantidad)
        self.total += detalle.preceio*detalle.cantidad
        self.detalleVent.append(detalle)

    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:15} Ruc: {}".format(empNombre,empRuc))
        print("Factura.N#: {:13} Fecha: {}".format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print("Linea Articulo       Precio Cantidad Subtotal")
        for det in self.detalleVent:
            print("{:5} {:10} {} {:6} {:7}".format(det.linea,det.articulo,det.descripcion,det.precio,det.cantidad))
            print("Total Venta:{:26}".format(self.total))


cli=Cliente("Ronny Vargas","120554545","064684165","villaPark")



Emp=Empresa()
cli1 = ClientePersonal("Ronny Vargas","120554545","064684165","villaPark",True)
print(cli1.getCedula())

art1=Articulo("aceitte",3,100)
art2=Articulo("cola",2,50)
art3=Articulo("cervezA",12,600)

today=date.today()
fecha=date(2021,8,15)

venta=CabVenta('F00001',date.today(),cli1)
venta.agregarDetalle(art1,3)
venta.agregarDetalle(art2,2)
venta.agregarDetalle(art2,1)
venta.mostrarVenta(Empresa.nombre,Empresa.ruc)


class InterfaceSistemaPago(ABC):
    @abstractclassmethod
    def pago(self):
        pass
    @abstractclassmethod
    def saldo(self):
        pass


class ImplePagoTargeta(InterfaceSistemaPago):
    # Este proceso se hace para el pago del calculo del interes de la Tarjeta
    def pago(self):
        return "Pago Targeta"
    
    def saldo(self):
        return "Saldo de Tarjeta reducida"

class ImplePagoContrato(InterfaceSistemaPago):
    def pago(self):
        return "Pago Contrato"
    
    def saldo(self):
        return "Saldo de Contrato reducido"

class Vendedor():
    def __init__(self,nombre):
        self.nombre=nombre
    
    def ModuloPago(self,contrato):
        return contrato.pago()


pagoTarjet= ImplePagoTargeta()
print(pagoTarjet.pago())
# pagoTarjet.pago()
pagoContrat=ImplePagoContrato()
#print(pagoContrat.pago())

ven1=Vendedor('ronny')
print(ven1.ModuloPago(pagoContrat))