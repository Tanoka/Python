import coloresAscii #Es un fichero en el mismo directorio donde he puesto las funciones para los
                    # colores para invocarlas hay que poner coloresAscii.funcion(param)

#variable global de este fichero, valor casilla mundo sin bacterias
vacio = 0

def checkEspacioCircundante(espacioCircundante, mundo, punto):
    """Comprueba el espacio indicado y retorna los parámetros que influyen para la vida 
    de las bacterias"""
    numVacio = 0
    contTipoBact = { 1:0, 2:0 }
    for x in range(espacioCircundante[0], espacioCircundante[1]+1): #hay que sumarle 1, pues es hasta ese número, pero no lo incluye
        for y in range(espacioCircundante[2], espacioCircundante[3]+1):
            if not (x == punto[0] and y == punto[1]):
                queBact = queBacteria(mundo, (x, y))
                if queBact != vacio:
                    contTipoBact[queBact] = contTipoBact[queBact] + 1 #obteniendo el total por cada
                                                                      # tipo de bacteria
                else:
                    numVacio = numVacio + 1 #de momento no se usa...    
    return (contTipoBact, numVacio)

def aplicaReglasVida(estadoEspacios, maxVida, minVida):
    "Aplica las reglas de la vida según los datos obtenidos sobre el estado de una zona"
    contTipoBact, esp = estadoEspacios
    totalVida = sum(contTipoBact.values()) #Casillas totales ocupadas por todos los tipos de bac.
    if (totalVida > maxVida) or (totalVida < minVida):
        return vacio 
    ganadoraBact = max(contTipoBact.values()) #bacteria que ocupa más casillas
    if estaRepetido(ganadoraBact, contTipoBact):
        return vacio # hay el mismo número de las bacterias con el mayor número.. no se dejan
                      #crecer la una a la otra
    tipoGanador = getIndxFromValInDict(ganadoraBact, contTipoBact)
    return tipoGanador[0]

def getIndxFromValInDict(valor, diccionario):
    "Retorna la key del valor buscado en un diccionario"
    return [key for (key, value) in diccionario.items() if value == valor]

def estaRepetido(bus, lista):
    "Función para ver si un valor está repetido en una lista"
    tmp = []
    for c in lista:
        if bus in tmp:
           return True
        else:
           tmp.append(c)
    return False

def getEspacioCircundate(mundo, punto):
    "Retorna el espacio del mundo que interactua con el punto dado"
    x_ini = 0 if punto[0] - 1 < 0 else punto[0] - 1
    x_end = punto[0] if punto[0] + 1 >= len(mundo) else punto[0] + 1
    y_ini = 0 if punto[1] - 1 < 0 else punto[1] - 1
    y_end = punto[1] if punto[1] + 1 >= len(mundo[0] ) else punto[1] + 1
    return (x_ini, x_end, y_ini, y_end)

def queBacteria(mundo, posicion):
    "Retorna el contenido de la posición indicada en el mundo de las bacterias"
    if mundo[posicion[0]][posicion[1]] == vacio:
        return False
    else:
        return mundo[posicion[0]][posicion[1]]

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

