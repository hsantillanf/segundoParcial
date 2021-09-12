
#menu principal
#1) CALCULADORAS
#2) NUMEROS
#3) LISTAS
#3) LISTAS
#5) SALIR
# elige la opcion [1...5]

#CALCULADORA Menu 
# 1)suma 
# 2)resta
#3)salir
from _typeshed import Self

class Menu:
    def __init__(self, titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

        
    def menuPrincipal(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("eliga la opcion[1...{}]".format(len(Self.opciones)))
        return opc 

obj=Menu("menu principal",["1) CALCULADORAS","2) NUMEROS","3) LISTAS","4) CADENAS","5) SALIR"])
opc =obj.menuPrincipal()

if opc == "1":
            obj=Menu("menu de calculadora",["1) suma","2) resta","3) salir"])
            opc1=obj.menuprincipal()
            if opc == "1":
                print("suma de 2 numeros")
                n1=int(input("ingrese n1: "))
                n2=int(input("ingrese n2: "))
                suma=n1+n2
                print("{}+{}={}".format(n1,n2,suma))

elif opc == "2":
        obj=Menu("menu numer",["1) perfecto","2) primo","3) salir"])
        opc2=obj.menuprincipal()


elif opc == "3":
            print("menu lista")
elif opc == "4":
            print("menu cadenas")
elif opc == "5":
            print("gracias por su visita...")

else:
            print("opcion no valida")

#menuPrincipal()


