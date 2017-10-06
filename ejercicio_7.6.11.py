def plegadoText(texto,longitud):
    pos=1
    posini=0
    long=15
    print(len(texto))
    while (long==15):
        textoNuevo=texto[posini:longitud+posini]
        long=len(textoNuevo)
        print("Texto Inicial: "+textoNuevo+"  ,longitud: "+str(long))
        if long==15:
            while textoNuevo[long-pos]!=" ":
                textoNuevo=texto[posini:(long-pos+posini)]
                pos+=1
        print("Texto final: "+textoNuevo)
        posini=posini+len(textoNuevo)-1
        print("Posini: "+str(posini))
        pos=1
    print(posini+longitud)
plegadoText("En un lugar de la mancha, de cuyo nombre no quiero acordarme, vivia un hidalgo...",15)