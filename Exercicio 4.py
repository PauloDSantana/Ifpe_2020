# Questao 4:

# Faça um programa que leia e monte duas listas
# contendo números inteiros com 10 itens cada.
# Depois de montados gere um terceiro vetor formado
# pela diferença dos dois vetores lidos, um quarto
# vetor formado pela soma dos dois vetores lidos e
# por último um quinto vetor formado pela multiplicação dos dois vetores lidos (2 pontos).

n = 0
lista1 = []
while True :
    numeros = (int (input("Digite os 10 numeros do primeiro Vetor 1 : ")))
    lista1.append(numeros)

    n += 1
    if n == 10:
     break

n = 0
lista2 = []
while True :
    numeros = (int(input("Digite os 10 numeros do segundo Vetor 2 : ")))
    lista2.append(numeros)

    n += 1
    if n == 10:
        break

lista3 = [lista1[0] - lista2[0], lista1[1]-lista2[1], lista1[2]-lista2[2],
          lista1[3]-lista2[3], lista1[4]-lista2[4], lista1[5]-lista2[5],
          lista1[6]-lista2[6], lista1[7]-lista2[7], lista1[8]-lista2[8],
          lista1[9]-lista2[9]]

print("O vetor DIFERENCA formado é = ")
print(lista3)

lista4 = [lista1[0]+lista2[0], lista1[1]+lista2[1], lista1[2]+lista2[2],
          lista1[3]+lista2[3], lista1[4]+lista2[4], lista1[5]+lista2[5],
          lista1[6]+lista2[6], lista1[7]+lista2[7], lista1[8]+lista2[8],
          lista1[9]+lista2[9]]

print("O vetor SOMA formado é = ")
print(lista4)


lista5 = [lista1[0]*lista2[0], lista1[1]*lista2[1], lista1[2]*lista2[2],
          lista1[3]*lista2[3], lista1[4]*lista2[4], lista1[5]*lista2[5],
          lista1[6]*lista2[6], lista1[7]*lista2[7], lista1[8]*lista2[8],
          lista1[9]*lista2[9]]

print("O vetor PRODUTO formado é = ")
print(lista5)