"""

"""
import math
import os
import random as rd
import time



cantDeSignal1 = 0
def getProbVect(S,lineas):
    global cantDeSignal1
    for i in lineas:
        if (i not in S):
          S[i] = 1
        else:
          S[i] = S[i]+1
    tam = len(lineas)
    for j in S:
        S[j] = S[j]/tam
        cantDeSignal1 += 1
    return S


def codificacion(arregloArbol,diccionario,codigo):
    if len(arregloArbol) == 2 and type(arregloArbol)!= str:
        codificacion(arregloArbol[0],diccionario,codigo+"1")
        codificacion(arregloArbol[1],diccionario,codigo+"0")
    else:
        diccionario[arregloArbol] = codigo


def calcEntropia(s):
    H=0
    for elem in s:
        prob = s[elem]
        hi = prob * math.log2(prob) * -1
        H = H + hi
    return H

def calcLongMedia(probs,cod):
    L=0
    for c in cod:
        L = L + probs[c] * len(cod[c])
    return L

def crearArbol(lista):
  while not(len(lista)== 1):
    listAux = [lista[0][0],lista[1][0]]
    auxProb = lista[0][1] + lista[1][1]
    lista.pop(0)
    lista.pop(0)
    lista.insert(0,(listAux,auxProb))
    lista = sorted(lista,key = lambda x: x[1])
  return lista[0][0]


def mediaConVectProb(vect):
    suma = 0
    for v in vect:
        suma += float(vect[v])*float(v)
    return suma

def mediaSimulacion(S):
    suma = 0
    N=0
    mediaAnt=-1
    mediaAct = 0
    while (not converge(mediaAnt,mediaAct) or  N < len(S)*4/5 ):
        suma += int(S[rd.randint(0,len(S)-1)])
        N+=1
        mediaAnt = mediaAct
        mediaAct = suma/N
    return mediaAct

def converge(m0,m1):
    sigma = 0.0001
    return abs((m1-m0))<sigma

def calcDesvioConProb(m,vec):
    suma = 0.0
    for v in vec:
        aux = math.pow((float(v) - m),2)
        suma += aux * vec[v]
    return math.sqrt(suma)

def calcDesvioMuestreo(S):
    suma = 0
    media = 0
    sumV = 0
    N=0
    varAnt = -1
    varAct = 0
    while (not converge(varAnt,varAct) or N < len(S)*4/5 ):
        rInt = rd.randint(0,len(S)-1)
        N+=1
        suma += float(S[rInt])
        media = suma / N
        sumV += math.pow(float(S[rInt])-media,2)
        varAnt = varAct
        varAct = sumV /N
    return math.sqrt(varAct)


Sig1 = open('signal1', 'r')
Sig2 = open('signal2', 'r')
S1 = Sig1.read()
S2 = Sig2.read()
TotalDeSimbolos = S1.split("\n")
setS1 = getProbVect({},S1.split("\n"))
H1 = calcEntropia(setS1)
lista = sorted(setS1.items(),key=lambda x: x[1])
arbol=crearArbol(lista)
diccionario = {}
codificacion(arbol,diccionario,"")
L1 = calcLongMedia(setS1,diccionario)
tamTotal = 0
for s in TotalDeSimbolos:
    tamTotal += len(diccionario[s])
print(tamTotal/8)

print(f"Para S1 La cantidad de bits será la longPromedio de la codificacion * la cantidad de elementos de la señal \n tam = {L1*len(TotalDeSimbolos)/8} Bytes Contra {os.stat('signal1').st_size} Bytes del archivo oriiginal \n .\
Entonces comprime {os.stat('signal1').st_size/(L1*len(TotalDeSimbolos)/8)}")
print(f"Señal 1: Entropia teorica = {H1}, LongMedia de codificacion = {L1}")
print(f"Por lo que el rendimiento de esta codificacion es de {L1/H1}")
media = mediaConVectProb(setS1)
print(f"La media obtenida con el vector de probabilidad es: {mediaConVectProb(setS1)}")
simbolosS1 = S1.split('\n')
print(f"La media mediante simulacion computacional es: {mediaSimulacion(simbolosS1)}")

print(f"Desvio con prob: {calcDesvioConProb(media,setS1)}")
print(f"Desvio por Muestreo: {calcDesvioMuestreo(simbolosS1)}")
setS2 = getProbVect({},S2.split("\n"))
H2 = calcEntropia(setS2)
lista = sorted(setS2.items(),key=lambda x: x[1])
arbol=crearArbol(lista)

diccionario = {}
codificacion(arbol,diccionario,"")
L2 = calcLongMedia(setS2,diccionario)
TotalDeSimbolos = S2.split("\n")
tamTotal = 0
for s in TotalDeSimbolos:
    tamTotal += len(diccionario[s])
print(tamTotal/8)
print(f"Para S2 La cantidad de bits será la longPromedio de la codificacion * la cantidad de elementos de la señal \n tam = {L2*len(TotalDeSimbolos)/8} Bytes Contra {os.stat('signal2').st_size} Bytes del archivo oriiginal \n .\
Entonces comprime {os.stat('signal1').st_size/(L1*len(TotalDeSimbolos)/8)}")

print(f"Señal 2: Entropia teorica = {H2}, LongMedia de codificacion = {L2}")
print(f"Por lo que el rendimiento de esta codificacion es de {L2/H2}")
media = mediaConVectProb(setS2)
print(f"La media obtenida con el vector de probabilidad es: {mediaConVectProb(setS2)}")
simbolosS2 = S2.split('\n')
print(f"La media mediante simulacion computacional es: {mediaSimulacion(simbolosS2)}")

print(f"Desvio con prob: {calcDesvioConProb(media,setS2)}")
print(f"Desvio por Muestreo: {calcDesvioMuestreo(simbolosS2)}")
