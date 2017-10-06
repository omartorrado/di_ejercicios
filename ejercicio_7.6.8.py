lista = ["Di","buen","día","a","papá"]

def listaNuevaReverse():
    listaNueva = []
    for x in lista:
        listaNueva.insert(-1,x)
    print(listaNueva)
    print(lista)

def listaReverse():
    lista.reverse()
    print(lista)

listaNuevaReverse()
listaReverse()