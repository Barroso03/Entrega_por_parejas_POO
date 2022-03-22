class Palindromo():
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
print("EJERCICIO PALINDROMO:")
print(Palindromo.palabrapalindromo("palabra"))