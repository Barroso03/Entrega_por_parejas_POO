# Entrega_por_parejas_POO


## Repositorio:

El link del repositorio es https://github.com/Barroso03/Entrega_por_parejas_POO



## Tarea:

La tarea que hemos realizado estaba basada en resolver unos ejercicios aplicando determinadas pautas que nos indican los ejercicios y además en la adjunción de UML´s.

## Integrantes:

1. [Juan](https://github.com/juaannavarro) 
2. [Barroso](https://github.com/Barroso03)



## Ejercicio a y b:

```
class palindromo():
  def __init__(self,palabra):
    self.palabra = palabra
  def palabrapalindromo(palabra):
    palabra = input("Seleccione una palabra:")
    if palabra == ''.join(reversed(palabra)):
      print("True")
      print(palabra.upper())
    else:
      print("False")
      print(palabra.upper())
print(palindromo.palabrapalindromo("palabra"))

````
UML:


<img width="215" alt="Captura de pantalla 2022-03-22 a las 9 56 11" src="https://user-images.githubusercontent.com/91721668/159443630-752bb9f1-b332-4c3d-bb30-7fe913dd9356.png">


## Ejercicio c:

```
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 
# Solucion: define dos funciones que son la de la Y y la de la Z y una variable que es la a, tras esto va operando con los resultados de la a, la Y y la Z


```

UML:

<img width="288" alt="Captura de pantalla 2022-03-22 a las 9 59 43" src="https://user-images.githubusercontent.com/91721668/159444497-2be8ff6b-e5f0-4988-8aa0-cc9b7b8b9f03.png">



## Ejercicio d:

```

class Logger():
    def log():
        print("--Start log--")
        for i in range(1,6):
            if i == 1:
                print("Primera llamada")
            else:
                print("{}ª llamada".format(i))
        print("--End log--:", "{}".format(i), "log (s)" )
print(Logger.log())        

```


UML:

<img width="254" alt="Captura de pantalla 2022-03-22 a las 10 01 13" src="https://user-images.githubusercontent.com/91721668/159444517-8b14d3dd-2682-4a59-a2c4-cef5dd2dc3bf.png">


