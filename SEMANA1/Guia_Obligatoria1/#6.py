'''6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
cuántas horas y minutos sobran.'''

def convertir_minutos(mins):
    horas= int(mins//60)
    sobrante= int(mins%60)
    return (horas,sobrante)
    
