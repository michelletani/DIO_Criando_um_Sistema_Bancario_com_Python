saldo = 0.0
limite = 500.0
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

opcoes = """
            Digite sua operação: 
                [1] Depósito
                [2] Saque
                [3] Extrato
                [4] Sair
            """

while True:

    operacao = int(input(opcoes))

    #------------------------------------Depósito----------------------------------------
    if (operacao == 1):
        valor_deposito = float(input("Digite o valor: "))

        if(valor_deposito > 0):
            saldo += valor_deposito
            extrato += f"+ {valor_deposito:.2f}\n"

        else:
            print("Valor inválido!")

        print(f"Saldo: {saldo:.2f}")

    #--------------------------------------Saque------------------------------------------
    elif (operacao == 2):
        
        if (numero_saque >= LIMITE_SAQUE):
            print("Limite de saques atingido.")
        
        valor_saque = float(input("Digite o valor: "))

        if (saldo < valor_saque):
            print(f"Saldo insuficiente. Saldo atual: {saldo:.2f}")
        
        elif (valor_saque > limite):
            print(f"Valor do saque excede o limite de {limite:.2f}.")
        
        else:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"- {valor_saque:.2f}\n"
            
            print(f"Saldo: {saldo:.2f}")

    #-------------------------------------Extrato-----------------------------------------
    elif (operacao == 3):
        if(extrato == ""):
            print("Nenhuma operação realizada.")

        else:    
            print("extrato:")
            print(extrato)

        print(f"Saldo: {saldo:.2f}")

    #-------------------------------------Encerrar----------------------------------------
    elif (operacao == 4):
        break 
        
    else:
        print("Não foi indentificada a operação.")

        