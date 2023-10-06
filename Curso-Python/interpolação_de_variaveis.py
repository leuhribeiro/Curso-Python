#old style "%" - não utilizar
#interpolação e colocar valores de variaveis que o usuario definiu em uma string 
#exemplo criar um sistema de certidicado donde passa onome  etc.

#metodo format  utiliza {} os locais que vai ser subistiuido a varivael e .format() a sequencia que precisa ser subistituido **precisa ser em sequencia senao da erro
# no format pode colocar entre chaves quais a posição da variavel que vc quer colocar na string, inicia no 0 


#nome=str(input("Digite seu Nome: "));


#print("Parabéns {nome} você foi aprovado no curso Python.".center(30,'#').format(nome=nome))


#fstring - nao precisa colcoar o comando no final tipo % ou .format 
#na f-string coloca {} e dentro da chave a variavel que vai ser subistituida tem que colocar o f na frente da string

nome= "Leonardo"
idade = 28
profissao = "Assistente de Engenharia"
linguagem= "Python"
# old style
print("Nome: %s Idade: %d"% (nome,idade))
# format
print("Nome: {} Idade: {}".format(nome,idade))
print("Nome: {0} Idade: {1}{1}{0}".format(nome,idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))

#f -string
print(f"{nome},{idade},{profissao},{linguagem}")