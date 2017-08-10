import coloresAscii #Es un fichero en el mismo directorio donde he puesto las funciones para los
                    # colores para invocarlas hay que poner coloresAscii.funcion(param)

#variable global de este fichero, valor casilla mundo sin bacterias
vacio = 0

def checkEspacioCircundante(espacioCircundante, tipoBacteria, mundo, punto):
    """Comprueba el espacio indicado y retorna los parámetros que influyen para la vida 
    de las bacterias"""
    numVacio = 0
    #creamos un dictionary para contar cuantas bacterias hay de cada tipo
    contTipoBact = { tipo: 0 for tipo in tipoBacteria.keys() }
    #hay que sumar 1 al segundo valor de range(), la lista debe incluir el número final 
    for x in range(espacioCircundante[0], espacioCircundante[1]+1): 
        for y in range(espacioCircundante[2], espacioCircundante[3]+1):
            if not (x == punto[0] and y == punto[1]): #no chequeamos el punto donde estamos
                queBact = mundo[x][y] #que bacteria hay en esa posicion
                if queBact != vacio:
                    #Obtenemos el total para cada tipo de bacteria
                    contTipoBact[queBact] = contTipoBact[queBact] + 1 
                else:
                    numVacio = numVacio + 1 #de momento no se usa...    
    return (contTipoBact, numVacio)

def aplicaReglasVida(estadoEspacios, maxVida, minVida):
    "Aplica las reglas de la vida según los datos obtenidos sobre el estado de una zona"
    contTipoBact, esp = estadoEspacios
    totalVida = sum(contTipoBact.values()) #Casillas totales ocupadas por todos los tipos de bac.
    if (totalVida > maxVida) or (totalVida < minVida):
        return vacio 
    ganadoraBact = max(contTipoBact.values()) #número mayor de un tipo de bacterias en las casillas
    if isRepetidoInDictionary(ganadoraBact, contTipoBact): #Está repetido ese ńumero de bacterias?
        return vacio # hay el mismo número de las bacterias con el mayor número.. no se dejan
                      #crecer la una a la otra
    return getIndxFromValInDictio(ganadoraBact, contTipoBact) #cual es la bacteria ganadoraBact?

def getIndxFromValInDictio(valor, diccionario):
    "Retorna la key del valor buscado en un diccionario"
    clave = [key for (key, value) in diccionario.items() if value == valor].pop()
    return clave

def isRepetidoInDictionary(bus, dictio):
    "Función para ver si un valor está repetido en un diccionario"
    return list(dictio.values()).count(bus) > 1 #dict.values() no es una lista real..es una view
        # object, para poder aplicar count hay que convertirlo en una lista real

def getEspacioCircundate(mundo, punto):
    "Retorna el espacio del mundo que interactua con el punto dado"
    x_ini = 0 if punto[0] - 1 < 0 else punto[0] - 1
    x_end = punto[0] if punto[0] + 1 >= len(mundo) else punto[0] + 1
    y_ini = 0 if punto[1] - 1 < 0 else punto[1] - 1
    y_end = punto[1] if punto[1] + 1 >= len(mundo[0] ) else punto[1] + 1
    return (x_ini, x_end, y_ini, y_end)

def estadoInicial(mundo, bacterias):
    "Introduce las bacterias en las posiones indicadas del mundo"
    for row in range(len(mundo)):
        for col in range(len(mundo[0])):
            for cepa in bacterias:
                for bact in cepa['pos']:
                    if bact[0] == row and bact[1] == col:
                        mundo[row][col] = cepa['tipo']
    return mundo

def printmundo(mundo, tipoBacteria):
    "Imprime en pantalla el mundo y sus bacterias"
    for x in range(len(mundo)):
        for y in range(len(mundo[0])):
            posi = mundo[x][y]
            if posi != vacio:   
                print(coloresAscii.bgLightGray(""), end="") #fondo de pantalla gris         
                print(coloresAscii.fgRed(tipoBacteria[posi]), end="") # end="" no imprime nueva linea
            else:
                print(coloresAscii.bgLightGray(""), end="") #fondo de pantalla gris
                print(" " + coloresAscii.resetColor(), end="")
        print();

def generadorMundo(ancho, alto):
    "Genera un array de array que representa al mundo de las bacterias"
    return [[vacio for n in range(ancho)] for row in range(alto)] 

