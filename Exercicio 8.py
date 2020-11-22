# Questao 8 :

# Usando o arquivo texto notas_estudantes.txt escreva um programa
# que calcula a média das notas de cada estudante e imprime o nome, a média (1 ponto).

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

cont_jose = len(jose)
cont_pedro = len(pedro)
cont_suzana = len(suzana)
cont_gisela = len(gisela)
cont_joao = len(joao)

contador_media = [cont_jose, cont_pedro, cont_suzana, cont_gisela, cont_joao]

def somatorio_lista(alunos):
   if len(alunos) == 1:
        return alunos[0]
   else:
        return alunos[0] + somatorio_lista(alunos[1:])

media_geral_jose = somatorio_lista(jose)/cont_jose

media_geral_pedro = somatorio_lista(pedro)/cont_pedro

media_geral_suzana = somatorio_lista(suzana)/cont_suzana

media_geral_gisela = somatorio_lista(gisela)/cont_gisela

media_geral_joao = somatorio_lista(joao)/cont_joao

print('A media das notas de Jose e {}'.format(media_geral_jose))
print('A media das notas de Pedro e {}'.format(media_geral_pedro))
print('A media das notas de Suzana e {}'.format(media_geral_suzana))
print('A media das notas de Gisela e {}'.format(media_geral_gisela))
print('A media das notas de Jose e {}'.format(media_geral_joao))