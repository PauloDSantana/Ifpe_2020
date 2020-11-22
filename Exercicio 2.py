# Question 2 Super Fatorial

#Faça uma função não-recursiva que receba um número inteiro positivo N
# e retorne o superfatorial desse número. O superfatorial de um número N
# é definida pelo produto dos N primeiros fatoriais de N.
# Assim, o superfatorial de 4 e sf(4) = 1! * 2! * 3! * 4! = 288  (2 pontos).

n = int(input('Digite um numero inteiro n:'))


while True:

    if n == 1 or n == 0:

        print("O Super fatorial e igual a : 1")
        break

    if n < 0:

        print("Numero invalido! Apenas valores inteiros positivos podem ser digitados:")
        break

    if n > 1:

        superfatorial = 0
        fatorial = 1
        count = 1
        acc = 1
        while count <= n:
         fatorial = fatorial*count
         acc = fatorial*acc
         count += 1

        break

print('O SuperFatorial de N! é = {}'.format(acc))

