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

def switch_case(opcao, saldo, extrato, numero_saques):
            
        if opcao == "d":
            valor = float(input("Informe um valor a ser depositado: "))

            if valor > 0:
                saldo += valor
                extrato  +=  f"Depósito: R$ {valor:.2f}\n"
                
            else:
                print("Operação falhou! O valor informado é inválido")
                    
        elif opcao == "s":
            valor = float(input("Informe um valor a ser sacado: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saque = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! Excedeu o limite de saldo")
            elif excedeu_saque:
                print("Operação falhou! Excedeu o limite de saques")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
        
        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("Saindo do sistema...")
            return saldo, extrato, numero_saques, True
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        return saldo, extrato, numero_saques, False
sair = False

while not sair:
    opcao= input(menu).lower()
    saldo, extrato, numero_saques, sair = switch_case(opcao, saldo, extrato, numero_saques)
