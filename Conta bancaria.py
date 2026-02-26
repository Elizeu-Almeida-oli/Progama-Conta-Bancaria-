saldo = 0
extrato = []

def mostrar_Menu ():
    print("\n-------------------------- Bem Vindo ao Banco Master  --------------------------")
    print(f"-------------------------- Seu saldo atual: R$ {saldo:.2f} --------------------------")
    print("-------------------------- Selecione a Opção desejada --------------------------")
    print("--------------------------        Opção 1: Depositar  --------------------------")
    print("--------------------------        Opção 2: sacar      --------------------------")
    print("--------------------------        Opção 3: extrato    --------------------------")
    print("--------------------------        Opção 4: encerrar   --------------------------")
    
def sacar():
    global saldo
    valor = float(input(" Digite o valor que voce quer Sacar: R$ "))
    
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato.append(f"saque R$ {valor:.2f}" )
        print("saque Realizado com Sucesso")
    else:
        print("Saldo Insuficiente ou Valor invalido. ")
        
def depositar ():
    global saldo
    valor = float(input("Digite o valor que voce quer depositar: R$ "))
    
    if valor > 0:
       saldo += valor
       extrato.append(f"Deposito R$ {valor:.2f}")
       print("Valor depositado com Sucesso")  
    else:
        print("valor invalido ou deu Erro no Deposito")
        
def ver_extrato():
    print("\n-------------------------- Extrato  -------------------------- ")
    
    if extrato:
        for operacao in extrato:
            print(operacao)      
    else:
        print("nenhuma operacao Realizada ainda.")
        
while True:
    mostrar_Menu()
    opcao = input("Escolha uma opcao: ")
    
    if opcao == '1':
        depositar()
        
    if opcao =='2':
        sacar()
        
    if opcao == '3':
        ver_extrato()

    if opcao == '4':
        print("\nEncerrando A operaçao Obrigado por utilizar nossos serviços.")
        break
        
else:
    print("Opçao invalida tente novamente")       
        