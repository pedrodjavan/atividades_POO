# QUESTAO 01
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome + " " + sobrenome
print(f"Bem-vindo(a), {nome_completo}")


# Questao 02
i = input("Digite uma frase: ")
print(f"Espaços em branco: {i.count(" ")}")


# Questao 03
nome =  input("Informe o nome: ")

for cont in range(len(nome)):
    print(nome[0:cont  + 1])
  
# Questao 04
numero = (input("Diga-me o numero: "))
if len(numero) == 8:
    print(f"9{numero[:4]}-{numero[4:9]}")

elif len(numero) < 8:
    print("Num pode!")

else:
    if numero[0] == '9':
        print(f"{numero[:5]}-{numero[5:9]}")
    else:
        print("Num pode!")

#Questao 05

frase = input("Diga-me uma frase: ")

quantidade_vogais = 0
indice_vogais = []

for i, letra in enumerate(frase):
    if letra.lower() in "aeiou":
        quantidade_vogais += 1
        indice_vogais.append(i)

print("Quantidade de vogais: ", quantidade_vogais)
print("Índice das vogais: ", indice_vogais)
