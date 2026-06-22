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
