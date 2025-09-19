'''3. Promedio de valores:
Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
de los valores.'''

Num_flo=[0.0]*6
Num_flo[0]=1
Num_flo[1]=2
Num_flo[2]=3
Num_flo[3]=4
Num_flo[4]=5
Num_flo[5]=6

sumatotal=0
for i in range(len(Num_flo)):
    sumatotal += Num_flo[i]

promedio=sumatotal/len(Num_flo)
print(f"el promedio de los elementos del array es: {promedio}")
