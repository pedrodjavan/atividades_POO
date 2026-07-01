# questao 1

def contagem_caracteres(texto):
    contagem = {}

    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem
    
texto = input("Diga-me uma frase ou uma palavra: ")
resultado = contagem_caracteres(texto)
print(resultado)

# questao 2
O pc bloqueia o site :(

# questao 3
  def mesclar_dicionarios(dicionario_1, dicionario_2):
        resultado = dicionario_1.copy()  
        for chave, valor in dicionario_2.items():
            if chave in resultado:
                 resultado[chave] = max(resultado[chave], valor)
            else:
                 resultado[chave] = valor

            return resultado


  
