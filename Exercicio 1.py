#  Questao 1 :

# Três amigos jogaram na mega-sena da virada. Caso eles ganhem,
# o prêmio deve ser repartido proporcionalmente ao valor que cada
# deu para a realização ̧ao da aposta. Faça a um programa que leia
# quanto cada apostador investiu, o valor do prêmio,
# e imprima quanto cada um ganharia do prêmio com base no valor investido (2 pontos)


premio = float (input("Informe o valor do premio em R$ :"))
apostador1 = (input("Informe seu o nome Apostador 1:"))
valor1 = float(input("Informe valor a ser investido em apostas em R$ :"))
apostador2= (input("Informe seu nome Apostador 2:"))
valor2 = float(input("Informe valor a ser investido em apostas em R$ :"))
apostador3 = (input("Informe seu nome Apostador 3:"))
valor3 = float(input("Informe valor a ser investido em apostas em R$ :"))

fatorA: float = valor1/(valor1 + valor2 + valor3)
fatorB: float = valor2/(valor1 + valor2 + valor3)
fatorC: float =valor3/(valor1 + valor2 + valor3)

valor_de_A = premio*fatorA
valor_de_B = premio*fatorB
valor_de_C = premio*fatorC

print("\n {} o valor de sua premiacao conforme valor investido é R$ {}".format(apostador1, valor_de_A))
print("\n {} o valor de sua premiacao conforme valor investido é R$ {}".format(apostador2, valor_de_B))
print("\n {} o valor do sua premiacao conforme valor investido é R$ {}".format(apostador3, valor_de_C))