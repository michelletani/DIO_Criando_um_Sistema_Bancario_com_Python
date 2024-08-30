saldo = 0.0
limite = 500.0
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

def operacao_selecionada(operacao):
    global saldo
    global limite
    global extrato
    global numero_saque
    global LIMITE_SAQUE

    #------------------------------------Depósito----------------------------------------
    if (operacao == 1):
        valor_deposito = float(input("Digite o valor: "))
        saldo += valor_deposito
        extrato += f"+ {valor_deposito:.2f}\n"

        print(f"Saldo: {saldo:.2f}")
    
    #--------------------------------------Saque------------------------------------------
    elif (operacao == 2):
        
        if (numero_saque >= LIMITE_SAQUE):
            print("Limite de saques atingido.")
            return
        
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
        print("extrato:")
        print(extrato)

    else:
        print("Nenhuma operação realizada.")


operacao = int(input("""Digite sua operação: 
                 1 - Depósito
                 2 - Saque
                 3 - Extrato
                 """))

operacao_selecionada(operacao)