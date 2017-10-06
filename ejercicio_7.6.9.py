
def empaquetar(lista):
    valorAnterior=None
    valorActual=None
    repeticionesValorActual=1
    empaquetado=[]
    for x in lista:
        valorAnterior=valorActual
        valorActual=x
        print(x)
        if valorAnterior==valorActual:
            repeticionesValorActual+=1
        elif valorAnterior!=None:
            empaquetado.append((valorAnterior,repeticionesValorActual))
            repeticionesValorActual=1
    empaquetado.append((valorAnterior, repeticionesValorActual))
    print(empaquetado)

empaquetar([1,1,1,3,5,1,1,3,3])



