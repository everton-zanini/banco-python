menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor à depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação não executada. valor informado é inválido")
    elif opcao == "s":
        valor = float(input("Digite o valor à sacar: "))
        execedeu_saldo = valor > saldo
        excedeu_limite = valor>limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou, você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou, O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou, Número máximo de saques excedido.")
        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou, o valor informado é inválido")

    elif opcao == "e":
        print("========================= EXTRATO ========================")
        print("Não foram realizados movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================================")

    elif opcao == "q":
        break
    else:
        print("Opção inválida...\n")