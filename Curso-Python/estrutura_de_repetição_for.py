#for e while -  são utilizado pra repetir trecho de codigo , por um determinado numero de vezes ou determinar por alguma expressaão logica

texto = input("Informe um texto:  ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")
else:
    print()
    print("Executa no final do laço")