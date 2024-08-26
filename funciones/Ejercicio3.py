#Crear una funcion que pida dos numeros.
#Si el primero es mayor al segundo, el programa debe retornar el valor 1;
#si el segundo es mayor al primero, debe retornar -1;
#si ambos son iguales, debe retornar 0

def retornar():
    a = int(input("Ingrese primer numero : "))
    b = int(input("Ingrese segundo numero : "))
    if a > b:
          return 1
    elif b > a:
         return -1
    else:
         return 0
    
print(retornar())
