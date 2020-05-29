''' Ejercicio sobre pilas '''

import os

# la clase Pilas
class Pilas:
  
  def __init__(self):
    self.pila=[]

  def __str__(self):
    cadena=''
    for pl in self.pila:
      cadena+=str(pl)+' '
    return(cadena)

  def Apila(self,valor):
    self.pila.append(valor)

  def Desapila(self):
    ultimo=self.pila[len(self.pila)-1]
    del self.pila[len(self.pila)-1]
    return ultimo

  def Cima(self):
    return self.pila[len(self.pila)-1]
    
  def Tamanio(self):
    return len(self.pila)

  def EsVacia(self):
    return len(self.pila)==0

# el menú:
def menu():
  opcion=''
  while not opcion in ['1','2','3','4','5','6','9','0']:
    os.system('cls')
    print('************  PILAS  ************')
    print()
    print(' Agregar nuevo valor a la pila  1')
    print(' Eliminar valor de la pila      2')
    print(' Mostrar último valor agregado  3')
    print(' Mostrar el tamaño de la pila   4')
    print(' ¿Está vacía?                   5')
    print(' Mostrar toda la pila           6')
    print(' Salir del programa             9')
    print()
    opcion=input(' Pulse 1,2,3,4,5,6 - 9: ')
    print()
  return opcion

# ****** Programa principal: *****

Pila=Pilas()
valor=0
accion='0'
while accion!='9':
  accion=menu()
  if accion=='1':
    valor=int(input('Introduzca un número: '))
    Pila.Apila(valor)
  elif accion=='2':
    if Pila.EsVacia():
      print('La pila está vacía')
    else:
      print('El último elemento {0} fue desapilado'.format(Pila.Desapila()))
  elif accion=='3':
    if Pila.EsVacia():
      print('La pila está vacía')
    else:
      print('El último elemento apilado: {0}'.format(Pila.Cima()))
  elif accion=='4':
    print('Tamaño de la pila: {0}'.format(Pila.Tamanio()))
  elif accion=='5':
    if Pila.EsVacia():
      print('La pila está vacía')
    else:
      print('La pila NO está vacía')
  elif accion=='6':
    if Pila.EsVacia():
      print('La pila está vacía')
    else:
      print(Pila)
  if accion!=1:
    input()
  os.system('cls')
