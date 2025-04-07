import textwrap

def menu():
    menu = """
    Bem vindo ao Sistema Bancário!
    Entre com a opção desejada:
    [1]\tSaque
    [2]\tDepósito
    [3]\tExtrato
    [4]\tNova conta
    [5]\tNovo Usuário
    [6]\tListar Contas
    [7]\tSair
    >>> """
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saque:
        print(f"@@@ Não é possível sacar R${valor},00. Tente novamente. @@@")

    elif excedeu_limite:
        print("@@@ Você já excedeu o limite de saques diários. @@@")

    elif excedeu_saldo:
        print("@@@ Você não tem limite. Verifique seu saldo e tente novamente. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saque += 1
        print(f"=== Saque de R${valor:.2f} Realizado com sucesso! ===")

    else:
        print("@@@ Valor incorreto, verifique os valores e tente novamente. @@@")

    return saldo, extrato

def depósito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito de realizado com sucesso! ===")
    else:
        print("\n@@@ Operação mal sucedida! Revise os valores e tente novamente. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n############ EXTRATO ############")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("####################################")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("@@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta Criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print ("@@@ Usuário não encontrado, verifique os dados e tente novamente! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main(): 
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    limite = 500
    numero_saque = 0
    usuarios = []
    contas = []


    while True:
        op = int(menu())
        
        if op == 1:
            valor = float(input("Digite o valor que irá sacar: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE,
            )

        elif op == 2:
            valor = float(input("Digite o valor que irá depositar: "))

            saldo, extrato = depósito(saldo, valor, extrato)

        elif op == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        elif op == 4:
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif op == 5:
            criar_usuario(usuarios)
        
        elif op == 6:
            listar_contas(contas)
        

        elif op == 7:
            print("Obrigado por utilizar nossos serviços!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

main()