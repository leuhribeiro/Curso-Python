#pode ter if dentro de if chamasse if aninhado

conta_normal=True
conta_universitaria=False

saldo=2000
cheque_especial=450
saque=int(input ("Digite o valor de saque: "))

if conta_normal:

    if saldo>=saque:
        print("Saque Realizado com sucesso!")
    elif saque<=(saldo+cheque_especial):
        print("Saque realizado com uso de cheque especial")    

elif conta_universitaria:
    if saldo>= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente!")

else:
    print("Sistema não reconheceu seu tipo de conta entre em contato com gerente")        