# estrutura condicional permite desvio de fluxo de controle pra fazer diversas açoes
#if - estrutra mais simples com um desvio
#if/else - estrutura com dois desvio
#if/elif/else 
#CNH
MAIOR_IDADE=18
IDADE_ESPECIAL=17
idade=int(input("Informe Sua idade: "))

if idade>= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade== IDADE_ESPECIAL:
    print("Pode realizar aulas téoricas, mas não realizar aulas práticas")

else :
    print("Ainda não pode tirar a CNH")


#pode ter if dentro de if chamasse if aninhado