import sys #Para poder obtener los parámetros que se pasan al script
import coloresAscii #Es un fichero en el mismo directorio donde he puesto las funciones para los
                    # colores para invocarlas hay que poner coloresAscii.funcion(param)

#Lo de la indentación es un conazo, mejorará con un IDE python?

#Cuidado con las asignaciones entre listas..recordar que toda asignacion es por referencia

#No ha constantes..todo esto son variables globales...

#No hace falta poner global en las funciones para acceder a variables locales a menos que queramos
# modificarlas

#tamaño mundo
if len(sys.argv) >= 3:
    try:
        ancho = int(sys.argv[1]) #cast. El contenido de argv es de tipo str
        alto = int(sys.argv[2])
    except ValueError:
        print("Altura y anchura deben ser valores numéricos")
        sys.exit(1)
else:
    ancho = 50
    alto = 6
#estados bacterias
muerte = 0
crece = 1
#estados mundo
vacio = 0
bacteria = 1
#ciclos
if len(sys.argv) >= 4:
    try:
        ciclos = int(sys.argv[3])
    except ValueError:
        print("El número de ciclos debe ser un valor numérico")
        sys.exit(1)
else:
    ciclos = 100
#max y min para vida
maxVida = 3 
minVida = 1
#coordenadas de bacterias iniciales
bacterias = [(1,2),(1,1),(1,3)]

print("Lineas:",alto," filas:", ancho, " ciclos:", ciclos)
input("Pulsa intro para continuar...")

def checkEspacioCircundante(espacioCircundante, mundo, punto):
	numBact = numVacio = 0
	for x in range(espacioCircundante[0], espacioCircundante[1]+1): #hay que sumarle 1, pues es hasta ese número, pero no lo incluye
		for y in range(espacioCircundante[2], espacioCircundante[3]+1):
			if not (x == punto[0] and y == punto[1]):
				if isBacteria(mundo, (x, y)):
					numBact = numBact + 1
				else:
					numVacio = numVacio + 1	#de momento no se usa...	
	return (numBact, numVacio)

def aplicaReglasVida(estadoEspacios):
	bact, esp = estadoEspacios
	if (bact > maxVida):
		return muerte
	if (bact < minVida):
		return muerte	
	return crece
		
def getEspacioCircundate(mundo, punto):
	x_ini = 0 if punto[0] - 1 < 0 else punto[0] - 1
	x_end = punto[0] if punto[0] + 1 >= alto else punto[0] + 1
	y_ini = 0 if punto[1] - 1 < 0 else punto[1] - 1
	y_end = punto[1] if punto[1] + 1 >= ancho else punto[1] + 1
	return (x_ini, x_end, y_ini, y_end)

def cambiarNuevoMundo(creceOmuere):
	if creceOmuere == muerte:
		return vacio
	elif creceOmuere == crece:
		return bacteria

def isBacteria(mundo, posicion):
	if mundo[posicion[0]][posicion[1]] == vacio:
		return False
	else:
		return True

def estadoInicial(mundo, bacterias):
	for row in range(alto):
		for col in range(ancho):
			for bact in bacterias:
				if bact[0] == row and bact[1] == col:
					mundo[row][col] = bacteria
	return mundo

def printmundo(mundo):
	for x in range(alto):
		for y in range(ancho):
			if mundo[x][y] == bacteria:	
				print(coloresAscii.bgLightGray(""), end="") #fondo de pantalla gris			
				print(coloresAscii.fgRed('*'), end="") # end="" no imprime nueva linea
			else:
				print(coloresAscii.bgLightGray(""), end="") #fondo de pantalla gris
				print(" " + coloresAscii.resetColor(), end="")
		print();

def generadorMundo():
    return [[vacio for n in range(ancho)] for row in range(alto)] 

mundo = generadorMundo()

mundo = estadoInicial(mundo, bacterias)
print ("mundo inicial")
printmundo(mundo)
print ("------------------------------")

newmundo = generadorMundo()

z = 0
while z < ciclos:
	for x in range(alto):
		for y in range(ancho):
			punto = (x, y)
			espacioCircundante = getEspacioCircundate(mundo, punto)
			estadoEspacios = checkEspacioCircundante(espacioCircundante, mundo, punto)
			creceOmuere = aplicaReglasVida(estadoEspacios)
			newmundo[x][y] = cambiarNuevoMundo(creceOmuere)	
	for x in range(alto):
		mundo[x] = newmundo[x][:] #copiar listas sin que sea por referencia. lista1 = lista2[:], lista1 = list(lista2)
	z = z + 1
	print("nuevo mundo ciclo ",z," ...................................")
	printmundo(mundo)

print ("FIN")
