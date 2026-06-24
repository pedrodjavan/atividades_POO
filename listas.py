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



