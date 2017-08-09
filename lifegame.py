import sys #Para poder obtener los parámetros que se pasan al script
from functionslife import * 
from bacteriasini import bacterias  #coordenadas de baterias iniciales

#Lo de la indentación es un conazo, mejorará con un IDE python?

#Cuidado con las asignaciones entre listas..recordar que toda asignacion es por referencia

#No ha constantes..todo esto son variables globales...

#No hace falta poner global en las funciones para acceder a variables locales a menos que queramos
# modificarlas

if '-h' in sys.argv or '--help' in sys.argv:
    print("-l número de ciclos")
    print("-s pausa cada número de ciclos indicado")
    print("-c número de columnas")
    print("-f número de filas")
    sys.exit(1)
#ciclos
if '-l' in sys.argv:
    ciclos = int(sys.argv[sys.argv.index('-l') + 1])
else:
    ciclos = 100

#pausas
if '-s' in sys.argv: #en caso de no estar saltaría una excepción..compruebo que está
    paso = int(sys.argv[sys.argv.index('-s') + 1])
else:
    paso = ciclos

#tamaño del mundo
if '-c' in sys.argv:
    try:
        ancho = int(sys.argv[sys.argv.index('-c') + 1])
    except ValueError:
        print("Anchura deben ser valores numéricos")
        sys.exit(1)
else:
    ancho = 50

if '-f' in sys.argv:
    try:
        alto = int(sys.argv[sys.argv.index('-f') + 1])
    except ValueError:
        print("Altura deben ser valores numéricos")
        sys.exit(1)
else:
    alto = 10

#max y min para vida
maxVida = 5 
minVida = 2 

############################
# main() 

tipoBacteria = {}
for cepa in bacterias:
    tipoBacteria[cepa['tipo']] =cepa['simbolo']

print("Líneas:",alto," filas:", ancho, " ciclos:", ciclos)
print("Bacterias: ", tipoBacteria)

mundo = generadorMundo(ancho, alto)

mundo = estadoInicial(mundo, bacterias)

print ("Mundo inicial")
printmundo(mundo, tipoBacteria)
input("Pulsa intro para continuar...")

newmundo = generadorMundo(ancho, alto)

z = 0
while z < ciclos:
    for x in range(alto):
        for y in range(ancho):
            punto = (x, y)
            espacioCircundante = getEspacioCircundate(mundo, punto)
            estadoEspacios = checkEspacioCircundante(espacioCircundante, mundo, punto)
            newmundo[x][y] = aplicaReglasVida(estadoEspacios, maxVida, minVida)
    for x in range(alto):
        mundo[x] = newmundo[x][:] #copiar listas sin que sea por referencia. lista1 = lista2[:], lista1 = list(lista2)
    z = z + 1
    print("nuevo mundo ciclo ",z," ...................................")
    printmundo(mundo, tipoBacteria)
    if z % paso == 0 and z != ciclos: #para que no pare en el último si coincide...
        input("Pulsa intro para continuar...")

print ("FIN")
