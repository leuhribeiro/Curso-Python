#maiusculo - .upper() *passa string para maiusculo
#minusculo - .lower() *passa a string para minusculo
#titulo - .title()  * o primeiro caracteres é maiusculo e o resto é minusculo
#cortar espaços na string
# remove espaço em branco da esquerda e direita - .strip()
# remove espaço em branco da  esquerda - .lstrip()
# remove espaço em branco da direita - .rstrip()
# junçoes e sentralização de string 
# center tem dois argumentos, com o numero de caracteres, e o caracteres para centralizar os caracteres - .center(n,"") *fazer menu
#join  funciona com todo tipo interavel, ele vai passar item a item e vai colocar o caractere definido pelo usuario - "".join()  * fazer lista melhorar e acessar arquivo

#upper lower e title
nome = "lEoNaRdO"

print(nome.upper())
print(nome.lower())
print(nome.title())

#strip
texto = "   Olá mundo!       "
print(texto+".")
print(texto.strip()+".")
print(texto.lstrip()+".")
print(texto.rstrip()+".")


# center e join

menu="Python"

print("####"+menu+"####")
print(menu.center(14,"#"))
print(menu.center(14))
print("*".join(menu))