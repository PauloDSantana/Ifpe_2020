# Questao 3
#
#Faça um programa que receba do usuário um novo de um arquivo texto existente.
# Crie um outro arquivo texto contendo o texto do arquivo de entrada,
# mas com as vogais substituídas por ‘*’ (1 ponto).



palavra = input('Digite um texto e substituirei as vogais por * (palavras sem acento!):\n')
palavra = palavra.replace("a", "*")
palavra = palavra.replace("e", "*")
palavra = palavra.replace("i", "*")
palavra = palavra.replace("o", "*")
palavra = palavra.replace("u", "*")


print(palavra)


