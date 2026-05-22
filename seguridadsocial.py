salariobase=float(input("ingrese slario base")) 
aportesalud=salariobase*0.04 
aportepension=salariobase*0.04
descuento=aportesalud+aportepension
salarioneto=salariobase-descuento 
print("El aporte a la salud es",aportesalud) 
print("el aporte a la pension es",aportepension)
print("su descuento es ",descuento)
print("su salario es",salarioneto) 
