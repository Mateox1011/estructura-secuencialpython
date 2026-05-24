cant=float(input("ingrese la cantidad de dinero a invertir: ")) 
periodo=float(input("ingrese el periodo de tiempo en años: "))
porsentajedeinteres=float(input("ingrese el porcentaje de interes anual: ")) 
valorinteres= (cant * porsentajedeinteres/100 * periodo)/360
print("el valor del interes es: ", valorinteres) 
valorimpuesto = valorinteres * 0.07
netopagar=cant+valorinteres-valorimpuesto
print("el valor neto a pagar es: ", netopagar) 
print("el valor del impuesto es: ", valorimpuesto) 
