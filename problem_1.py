# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 2 - Problem 1
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Quatro números inteiros v1, v2, v3 e v4.
Exemplo 1:
Digite o valor A: 5
Digite o valor B: 6
Digite o valor C: 7
Digite o valor D: 8
Exemplo 2:
Digite o valor A: 2
Digite o valor B: 3
Digite o valor C: 2
Digite o valor D: 6

Processes:
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos.", senão escrever "Valores recusados.".

Output(s):
Mostre a respectiva mensagem após a validação dos valores.
Exemplo 1:
Valores recusados.
Exemplo 2:
Valores aceitos.


"""


def main():
   a = int(input(f"Digite o valor A: 5"))
   b = int(input(f"Digite o valor B: 6"))
   c = int(input(f"Digite o valor C: 7"))
   d = int(input(f"Digite o valor D: 8"))

   if b > c and d > a and (c + d) > (a+ b) and c > 0 and d > 0 and a %2 == 0:
       print ("Valores aceitos.")
   else:
       print ("Valores recusados.")

if __name__ == '__main__':
    main()
