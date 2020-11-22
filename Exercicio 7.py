# Questao 7 :

# Usando o arquivo texto notas_estudantes.txt escreva um programa que
# imprime o nome dos alunos que têm mais de seis notas (1 ponto).

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

cont_jose = len(jose)
cont_pedro = len(pedro)
cont_suzana = len(suzana)
cont_gisela = len(gisela)
cont_joao = len(joao)

if cont_joao > 5 :
    print("Joao")

if cont_pedro > 5 :
    print("Pedro")

if cont_suzana > 5 :
    print("Suzana")

if cont_gisela > 5 :
    print("Gisela")

if cont_jose > 5 :
    print("Joao")
