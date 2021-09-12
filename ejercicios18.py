class Empresa:
    def __init__(self,nom="Extermix",ruc="0999959844",telf="064684165",dir="nice to me too"): #parametros crear para que sea mas generico.
        self.nombre=nom
        self.ruc=ruc
        self.telefono=telf
        self.direccion=dir

    def mostrarEmpresa(self):
        print('Empresa:{:15} Ruc:{} Telefono:{} Direccion:{}'.format(self.nombre,self.ruc,self.telefono,self.direccion))
    
class Cliente:
    def __init__(self,nom,ced,telf,dir):
        self.nombre=nom
        self.cedula=ced
        self.telefono=telf
        self.direccion=dir

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
    def __init__(self,nom,ced,telf,dir,descuento=True):
        super().__init__(nom,ced,telf,dir)
        self.__descuento = descuento

    @property #getter nos sirve para obetener el valor privado
    def descuento(self):
        if self.__descuento == True:
            return "Usted tiene 15% de Descuento"
        else:
            return "No recibe ningun Descuento"

    @descuento.setter #setter asigna un valor al atrivuto privado
    def descuento(self,value):
        self.__descuento=value

    def mostrarCliente(self):
        print('Nombre:{:15}'.format(self.nombre),self.descuento)

Emp=Empresa()

cli1= Cliente("Ronny Vargas","120554545","064684165","villaPark")
cli1.mostrarCliente()

cli2 = ClienteCorporativo("Ronny Vargas","120554545","064684165","villaPark",'01')
cli2.mostrarCliente()

cli3 = ClientePersonal("Ronny Vargas","120554545","064684165","villaPark",True)
cli3.mostrarCliente()
