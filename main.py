from usuario import User
import os

os.system('cls')

clientes=[]
for i in range(1,3):
    nombre=input("Ingresa Nombre Cliente "+str(i)+"°: ")
    
    correo=input("Ingresa Correo Cliente "+str(i)+"°: ")
    cliente = User(nombre, correo)
    clientes.append(cliente)

for i in clientes:
    os.system("cls")

    print("NOMBRE   -   CORREO   -   MONTO")
    print(" -------------------------------")
    for cliente in clientes:
        nom, cor, amo = cliente.situacion()
        print(" {:8} - {:4} - {:8}".format(nom, cor,amo))
    print()

    for cliente in clientes:
        
        if cliente == clientes[0]:
            for j in range(3):
                deposito = int(input(" {}, cuánto dinero desea depositar: ".format(cliente.nombre)))
                cliente.make_deposit(deposito)
            for k in range(1):
                retiro = int(input(" {}, cuánto dinero desea retirar: ".format(cliente.nombre)))
                cliente.make_withdrawal(retiro)
        if cliente == clientes[1]:
            for j in range(2):
                deposito = int(input(" {}, cuánto dinero desea depositar: ".format(cliente.nombre)))
                cliente.make_deposit(deposito)
            for k in range(2):
                retiro = int(input(" {}, cuánto dinero desea retirar: ".format(cliente.nombre)))
                cliente.make_withdrawal(retiro)
     
