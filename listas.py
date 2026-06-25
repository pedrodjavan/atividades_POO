# questão 01
pares = []
impares = []
p = int(input("Diga-me a quantidade de números: "))
if p < 0 or p < 4:
    print("Num pode!!")
else: 
    lista = []
    for i in range(0, p):
        num = int(input("Número: "))
        lista.append(num)
    print(f"Lista completinha\n{lista}")
    print(f"\nOs três primeiros\n{lista[0], lista[1], lista[2]}")
    print(f"Os dois ultimos\n{lista[p - 2], lista[p - 1]}")
    lista.reverse()
    print(f"Lista Invertida\n{lista}")

for i in range(0, p):
  if lista[i] % 2 == 0:
    pares.append(lista[i])
  else:
    impares.append(lista[i])
  print(f"Pares\n{pares}")
  print(f"Impares\n{impares}")



# questao 02
urls = [
    "www.reddit.com",
    "www.yahoo.com",
    "www.github.com",
    "www.google.com"
]

dominios = [url[4:-4] for url in urls]

print(dominios)


# questao 03
from random import randint

lista = [randint(-100, 100) for _ in range(20)]

lista_ordenada = sorted(lista)

indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

soma = sum(lista)
media = soma / len(lista)

print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
print("Soma dos valores:", soma)
print("Média dos valores:", media)

# questao 04

lista_1 = list(map(int, input("Diga-me os números da primeira lista: ").split()))
lista_2 = list(map(int, input("Diga-me os números da segunda lista: ").split()))

lista_3 = []
menor_tamanho = min(len(lista_1), len(lista_2))

for i in range(menor_tamanho):
    lista_3.append(lista_1[i])
    lista_3.append(lista_2[i])

if len(lista_1) > len(lista_2):
    lista_3.extend(lista_1[menor_tamanho:])
else:
    lista_3.extend(lista_2[menor_tamanho:])

print("Lista intercalada:", lista_3)



# questao 05

from random import randint

lista_1 = [randint(0, 50) for _ in range(20)]
lista_2 = [randint(0, 50) for _ in range(20)]
i = sorted(list(set(lista_1) & set(lista_2)))

print("Lista 1:", lista_1)
print("Lista 2:", lista_2)
print("Interseção:", i)



# questao 06 

não consegui fazer essa e questão 7 :(
















