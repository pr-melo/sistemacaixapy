menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor do depósito"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é invalido")
    
    elif opção == "s":
        valor = float(input("Informe o valor do saque"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaçãp falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operaçãp falhou! Você não tem limite suficiente.")

        elif excedeu_saques:
            print("Operaçãp falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operaçãp falhou! O valor informado é inválido.")

    elif opção == "e":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\Saldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opção == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")