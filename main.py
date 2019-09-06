from random import choice, randint
from fractions import Fraction
def mod(valor):
    return abs(2 - (float(valor)*float(valor)))
    
def criaListaCemStrings01():
    saida = []
    for i in range(100):
        p = ''
        for i in range(8):
            p+=''+str(randint(0, 1))
        saida.append(p)
    return saida

def num02 (listaFuncao):
    novaLista = []
    num = 1 
    for item in listaFuncao:
        listaAdd = [item, num] 
        
        novaLista.append(listaAdd)
         
    return novaLista

def trocaTroca(string1, string2):
    str1 = string1[0:4]+string2[4::]
    str2 = string2[0:4]+string1[4::]

    return str1

def motacao(string):
    split = [i for i in string]
    r = ''
    i = randint(0, len(split)-1)
    if (split[i]=='0'):
        split[i] = '1'
    else:
        split[i] = '0'
    return r.join(split)

def strNum(string, valor):
    return [string, valor]

def convertBinaPraReal(valor):
    part1 = int(str(valor[0])+''+str(valor[1]), 2)
    cont = 1
    part2 = 0.0
    for i in valor[2::]:
        part2 = part2 + Fraction(int(i), 2**cont)
        cont+=1
    final = int(part1)+part2
    return final

def dezMenoresAval(lista):
    return sorted(lista, key = lambda x: (x[1], x[0]))

def realToBinario(valor):
    vsplit = str(valor).split(".")#split do valor pelo ponto
    part1 = bin(int(vsplit[0]))[2::]#converte a primeira parte pra binario
    l = []
    ljoin = ''
    part2 = float(str(0)+'.'+vsplit[1])#pega a segunda parte adicona 0. ex.: 1.25 fica 0.25
    r = part2*2 #multiplica por 2 para converter a segunda parte para binario 
    l.append(str(r).split('.').pop(0)) #pega a parte inteira e coloca no vetor
    for i in range(len(vsplit[1])-1):
        r= float('0.'+str(r).split('.')[1])*2
        l.append(str(r).split('.').pop(0)) #pega a parte inteira e coloca no vetor
    final = str(part1)+'.'+(ljoin.join(l))
    return final
def validaCromossomo(dna, pesoObj):
    peso = 0
    for i in range(len(dna)-1):
        if(dna[i]=="1"):
            peso += pesoObj[i]
    return peso <= 22, peso

def calculaAptidao(dna, valorObjeto, pesoObj):
    aptidao = -1
    verifica = validaCromossomo(dna, pesoObj)
    if (verifica[0]):
        for i in range(len(dna)-1):
            if(dna[i]=='1'):
                aptidao += valorObjeto[i]
        

    return aptidao, verifica[1]