# Entrega_por_parejas_POO



# Ejercicio a y b:

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


# Ejercicio c:

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


# Ejercicio d:

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

UML:
