import main
def principal(valor):
    
    cemStringReal = []
    stringAvaliacao = []
    novaStrAval = []
    for i in range(len(valor)):
        cemStringReal.append(main.convertBinaPraReal(valor[i]))

    for i in range(len(cemStringReal)):
        stringAvaliacao.append(main.strNum(valor[i], main.mod(cemStringReal[i])))
    return stringAvaliacao

def avaliaPox0(valor):
    
    dezMenoresAval = main.dezMenoresAval(valor)[:10]
    
    rearanjo90 = []
    lista90mais10 = []
    l = []
    for i in range(len(dezMenoresAval)):
        for j in range(len(dezMenoresAval)):
            if(i!=j):
                str1 = main.trocaTroca(dezMenoresAval[i][0], dezMenoresAval[j][0])
                l.append(str1)

    for i in range(len(l)):
        rearanjo90.append([l[i], main.mod(main.convertBinaPraReal(l[i]))])   
    dezStr = []
    lista = []
    l1 = []
    for i in range(10):
        lista.append(rearanjo90[main.choice(range(len(rearanjo90)))][0])
        troca = main.motacao(lista[i])
        l1.append(troca)
        dezStr.append([l1[i], main.mod(main.convertBinaPraReal(l1[i]))])
    

    lista90mais10 = rearanjo90
    for i in dezStr:
        lista90mais10.append(i)

    return lista90mais10

lista100Strings01 = main.criaListaCemStrings01()


beneficio = [1, 4, 3, 20, 1, 9, 1, 2]
peso =      [7, 8, 4, 1, 9, 4, 6, 4]
calculaAptidao = []
cromossomo = []

lista100Strings01 = avaliaPox0(principal(lista100Strings01))

def prog(lista):
    k = 0
    while k <= 20:
        print("Geração {}:\n".format(k))
        lista100Strings01 = avaliaPox0(lista)
        for i in range(len(lista100Strings01)):
            cromossomo.append( lista100Strings01[i][0])
        for i in range(len(cromossomo)):
            calculaAptidao.append([cromossomo[i], main.calculaAptidao(cromossomo[i], beneficio, peso)])
        bene = 0
        for i in range(len(calculaAptidao)):
            
            if(20 < calculaAptidao[i][1][0] <= 22 and bene <= calculaAptidao[i][1][1]):
                bene = calculaAptidao[i][1][1]
                print("Cromossomo: "+calculaAptidao[i][0], ", Peso total de itens:", calculaAptidao[i][1][1], ", Beneficio:", calculaAptidao[i][1][0])
        k = k+1

prog(lista100Strings01)