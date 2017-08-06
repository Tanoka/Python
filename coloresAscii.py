#imprimir ASCII en colores.. son código que se ponen antes del caracter
def resetColor(): return "\033[00m"

def fgRed(prt): return "\033[91m"+ prt +"\033[00m"
def fgGreen(prt): return "\033[92m"+ prt +"\033[00m"
def fgYellow(prt): return "\033[93m"+ prt +"\033[00m"
def fgLightPurple(prt): return "\033[94m"+ prt +"\033[00m"
def fgPurple(prt): return "\033[95m"+ prt +"\033[00m"
def fgCyan(prt): return "\033[96m"+ prt +"\033[00m"
def fgLightGray(prt): return "\033[97m"+ prt +"\033[00m"
def fgBlack(prt): return"\033[98m"+ prt +"\033[00m"

def bgLightGray(prt): return "\033[47m"+ prt
def bgBlack(prt): return "\033[40m"+ prt
def bgGreen(prt): return "\033[42m"+ prt
def bgGrange(prt): return "\033[43m"+ prt
def bgBlue(prt): return "\033[44m"+ prt
def bgPurple(prt): return "\033[45m"+ prt
def bgCyan(prt): return "\033[46m"+ prt