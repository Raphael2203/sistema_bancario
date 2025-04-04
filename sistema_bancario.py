menu = """
Bem vindo ao Sistema Bancário!
Entre com a opção desejada:
[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair
>>> """

saldo = 0
extrato = ""
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    op = int(input(menu))
    
    if op == 1:
        saque = int(input("Valor que deseja realizar o saque: "))

        excedeu_saque = saque > limite
        excedeu_tentativas = numero_saque > LIMITE_SAQUE
        excedeu_saldo = saque > saldo

        if excedeu_saque:
            print(f"Não é possível sacar R${saque},00. Tente novamente.")
        elif excedeu_tentativas:
            print("Você já excedeu o limite de saques diários.")
        elif excedeu_saldo:
            print("Você não tem limite. Verifique seu saldo e tente novamente.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            print(f"Saque de R${saque:.2f} Realizado com sucesso!")

    elif op == 2:
        deposito = int(input("Digite o valor que irá depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito realizado com sucesso!")

        else:
            print("Operação mal sucedida! Revise os valores e tente novamente.")

    elif op == 3:
        print("\n############ EXTRATO ############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("####################################")

    elif op == 4:
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Opção inválida. Tente novamente.")