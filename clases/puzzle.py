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
