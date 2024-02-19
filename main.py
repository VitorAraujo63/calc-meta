print(60 *"=")
salario = float(input("Qual sua renda mensal: R$ "))
print(60 *"=")
meta = float(input("Qual sua meta? R$"))
print(60 *"=")
rest = float(input("Quanto por mes você guarda? R$ "))
print(60 *"=")



while True:
    print(60 *"=")
    n3 = int(input("Digite o que você gostaria de saber: \n 1 - Enquanto tempo você vai chegar na sua meta \n 2 - Qual o total você tera sem gastar nada \n 3 - alterar o valor da sua meta \n 4 - Suas informações \n 5 - Sair  \n Numero: "))
    print(60 *"=")

    if n3 == 1:
        esc = int(input("O que você quer: \n 1- saber com o valor que você guarda por mês \n 2- saber com outro valor de sua escolha \n Numero: "))
        if esc == 1:
            newm = meta/rest
            print(60 *"=")
            print(f"Se você guardar R${rest} por mês você chegara na sua meta em {newm:.0f} meses")

        elif esc == 2:
            newr = float(input("Qual valor você deseja? R$ "))
            n1 = meta/newr
            print(60 *"=")
            print(f"Com o novo valor de R${newr} você levaria {n1:.0f} meses")
        else:
            print(60 *"=")
            print("Valor enserido não encontrado, tente novamente...")
    elif n3 == 2:
        mesg = int(input("Por quantos meses gostaria de guardar o seu salario? R$ "))
        n2 = mesg*salario
        print(60 *"=")
        print(f"Se você guardasse o seu salario R${salario} por {mesg} meses, você teria um total acumulado em sua conta de R${n2}")
    elif n3 == 3:
        meta = float(input("Qual o novo valor da sua meta? R$ "))
    elif n3 == 4:
        print(60 *"=")
        print(f"SUAS INFORMAÇÕES: \n Salario: R${salario} \n Meta: R${meta} \n Valor Guardado por mês: R${rest}")
    elif n3 == 5:
        exit()
    else:
        print(60 *"=")
        print("\n O valor inserido não é valido. Tente novamente...\n") 
        print(60 *"=")   
