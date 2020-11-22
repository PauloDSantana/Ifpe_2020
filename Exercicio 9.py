# Questao 9
#
# Usando o arquivo texto notas_estudantes escreva um programa
# que calcula a nota mínima e máxima de cada estudante e imprima
# o nome de cada aluno junto com a sua nota máxima e mínima (1 ponto).

# jose 10 15 20 30 40
# pedro 23 16 19 22
# suzana 8 22 17 14 32 17 24 21 2 9 11 17
# gisela 12 28 21 45 26 10
# joao 14 32 25 16 89

jose = [10, 15, 20, 30, 40]
pedro = [23, 16, 19, 22]
suzana = [8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
gisela = [12, 28, 21, 45, 26, 10]
joao = [14, 32, 25, 16, 89]
alunos = [jose, pedro, suzana, gisela, joao]


# Maxima e Minima Media Jose

maximo_jose = jose[0]
for e in jose:
     if e > maximo_jose:
         maximo_jose = e

minimo_jose = jose[0]
for e in jose:
    if e < minimo_jose :
        minimo_jose = e
print("A menor media de Jose foi {} e a maxima media foi {}.".format(minimo_jose,maximo_jose))


# Maxima e Minima Media Pedro

maximo_pedro = pedro[0]
for e in pedro:
     if e > maximo_pedro:
         maximo_pedro = e

minimo_pedro = pedro[0]
for e in pedro:
    if e < minimo_pedro :
        minimo_pedro = e
print("A menor media de Pedro foi {} e a maxima media foi {}.".format(minimo_pedro,maximo_pedro))

# Maxima e Minima Media Suzana

maximo_suzana = suzana[0]
for e in suzana:
     if e > maximo_suzana:
         maximo_suzana = e

minimo_suzana = suzana[0]
for e in suzana:
    if e < minimo_suzana :
        minimo_suzana = e
print("A menor media de Suzana foi {} e a maxima media foi {}.".format(minimo_suzana,maximo_suzana))


# Maxima e Minima Media Gisela

maximo_gisela = gisela[0]
for e in gisela:
     if e > maximo_gisela:
         maximo_gisela = e

minimo_gisela = gisela[0]
for e in gisela:
    if e < minimo_gisela:
        minimo_gisela = e
print("A menor media de Gisela foi {} e a maxima media foi {}.".format(minimo_gisela,maximo_gisela))


# Maxima e Minima Media Joao

maximo_joao= joao[0]
for e in joao:
     if e > maximo_joao:
         maximo_joao = e

minimo_joao= joao[0]
for e in joao:
    if e < minimo_joao :
        minimo_joao = e

print("A menor media de Joao foi {} e a maxima media foi {}.".format(minimo_joao,maximo_joao))