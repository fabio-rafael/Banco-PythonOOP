from contas import *
from menus import *


conta_atual = None  # Inicialmente, nenhuma conta criada
menu_atual = 1  

while True:
    if menu_atual == 1:
        exibir_menu1()
        escolha = input("--> ")

        if escolha == "1":
            print("\nIntroduza o nome do titular da conta: ", end='')
            nome_conta = input()
            print("\nQual o seu depósito inicial: ", end='')
            quantia_inicial = input()
            
            # Verifica se o arquivo de dados da conta já existe
            try:
                with open('dados_contas.txt', 'r', encoding='latin-1') as arquivo:
                    # Se existir, tenta carregar as informações da conta
                    linhas = arquivo.readlines()
                    for linha in linhas:
                        if "Nome:" in linha:
                            conta_nome = linha.split(":")[1].strip()
                            if conta_nome == nome_conta:
                                print(f"\nA conta com o nome '{nome_conta}' já existe. Por favor, escolha outro nome.\n")
                                break
                    else:
                        # Se a conta não existir, cria a conta normalmente
                        with open('dados_contas.txt', 'a', encoding='latin-1') as arquivo:
                            arquivo.write(f"Nome: {nome_conta}\n")
                            arquivo.write(f"Quantia Inicial: {quantia_inicial}\n")
                            conta_atual = Conta(nome_conta, quantia_inicial)
                            conta_atual.getBalanco()
                            print("**********Conta criada com sucesso*********")
                            print("*******************************************\n")
                            menu_atual = 2  # Mudar para o segundo menu
            except FileNotFoundError:
                # Se o arquivo não existir, cria a conta normalmente
                with open('dados_contas.txt', 'w', encoding='latin-1') as arquivo:
                    arquivo.write(f"Nome: {nome_conta}\n")
                    arquivo.write(f"Quantia Inicial: {quantia_inicial}\n")
                    conta_atual = Conta(nome_conta, quantia_inicial)
                    conta_atual.getBalanco()
                    print("*******************************************\n")
                    menu_atual = 2  # Mudar para o segundo menu

        elif escolha == "2":
            nome_conta = input("Insira o nome do titular: ")
            conta_encontrada = False

            try:
                with open('dados_contas.txt', 'r', encoding='latin-1') as arquivo:
                    linhas = arquivo.readlines()

                    for index, linha_conta in enumerate(linhas):
                        if "Nome:" in linha_conta:
                            conta_nome = linha_conta.split(":")[1].strip()
                            if conta_nome == nome_conta:
                                for linha_quantia in linhas[index + 1:]:
                                    if "Quantia Inicial:" in linha_quantia:
                                        try:
                                            conta_quantia = float(linha_quantia.split(":")[1].strip())
                                            conta_atual = Conta(conta_nome, conta_quantia)
                                            conta_encontrada = True
                                            break
                                        except ValueError:
                                            print("\nErro ao carregar informações da conta. Por favor, contate o suporte.\n")
                                            break
                                break

                    if conta_encontrada:
                        print("\nBem-vindo de volta, ", conta_atual.nome)
                        conta_atual.getBalanco()
                        print("*******************************************\n")
                        menu_atual = 2  # Mudar para o segundo menu
                    else:
                        print(f"\nA conta com o nome '{nome_conta}' não foi encontrada. Por favor, crie uma nova conta.\n")

            except FileNotFoundError:
                print("\nVocê ainda não criou uma conta. Por favor, escolha a opção 1 para criar uma conta. \n")
        elif escolha == "3":
            elim = input("Digite o nome do titular da conta que pretende eliminar: ")

            with open('dados_contas.txt', 'r', encoding='latin-1') as arquivo:
                linhas = arquivo.readlines()
                encontrou_titular = False

                for index, linha_conta in enumerate(linhas):
                    if "Nome:" in linha_conta and elim in linha_conta:
                        # Encontrou o titular
                        encontrou_titular = True
                        conta_nome = linha_conta.split(":")[1].strip()

                        # Verificar se o nome corresponde exatamente
                        if conta_nome == elim:
                            # Remover as linhas associadas a este titular
                            linhas = linhas[:index] + linhas[index + 2:]
                            print(f"O titular {elim} foi removido com sucesso.")
                            break  # Não é necessário continuar a procurar

                if not encontrou_titular:
                    print("Esse titular não existe na base de dados!")

            # Escrever as linhas atualizadas de volta ao arquivo
            with open('dados_contas.txt', 'w', encoding='latin-1') as arquivo:
                arquivo.writelines(linhas)
        elif escolha == "4":
            print("\nSimular conta poupança / investimento a prazo  ...")
            nome = input("Introduza o seu nome: ")
            quantia = float(input("Qual o seu depósito inicial: "))
            taxa_juros_percentual = float(input("Qual a taxa de juros anual [%]: "))
            conta_poupanca = contaPoupanca(quantia, nome)
            conta_poupanca.set_taxa_percentual(taxa_juros_percentual)
            anos_simulacao = int(input("Quantos anos deseja simular: "))
            conta_poupanca.simular_impacto_anual(anos_simulacao)
            
        elif escolha == "9":
            print("\nLogout ... ")
            break

        else:
            print("\nOpção inválida. Por favor, digite um número válido!\n")



###########################################################################################################################################
                            ###########MENU2############
###########################################################################################################################################





    elif menu_atual == 2:
        exibir_menu2()
        escolha = input("--> ")

        if escolha == "1":       # saldo
            conta_atual.getBalanco()
            print("*******************************************\n")

        elif escolha == "2":    # depósito
            quantia = input("Qual o montante que deseja depositar :")
            conta_atual.deposito(quantia)
            with open('dados_contas.txt', 'r+', encoding='latin-1') as arquivo:
                linhas = arquivo.readlines()
                for index, linha_conta in enumerate(linhas):
                    if "Nome:" in linha_conta and conta_atual.nome in linha_conta:
                        # Encontrou o titular
                        linhas[index + 1] = f"Quantia Inicial: {conta_atual.balanco}\n"
                        break

                # Voltar para o início do arquivo e reescrever as linhas atualizadas
                arquivo.seek(0)
                arquivo.writelines(linhas)
                arquivo.truncate()
                    
            print("*******************************************\n")

        elif escolha == "3":   # levantamento
            quantia = input("Qual o montante que deseja levantar :")
            conta_atual.levantamento(quantia)
            with open('dados_contas.txt', 'r+', encoding='latin-1') as arquivo:
                linhas = arquivo.readlines()
                for index, linha_conta in enumerate(linhas):
                    if "Nome:" in linha_conta and conta_atual.nome in linha_conta:
                        # Encontrou o titular
                        linhas[index + 1] = f"Quantia Inicial: {conta_atual.balanco}\n"
                        break

                # Voltar para o início do arquivo e reescrever as linhas atualizadas
                arquivo.seek(0)
                arquivo.writelines(linhas)
                arquivo.truncate()
            print("*******************************************\n")

        elif escolha == "4":   # Transferência
            nome_conta_2 = input("Qual o titular da conta para a qual pretende transferir dinheiro? ")
            try:
                with open('dados_contas.txt', 'r', encoding='latin-1') as arquivo:
                    linhas = arquivo.readlines()
                    conta_origem = None
                    conta_destino = None

                    for index, linha_conta in enumerate(linhas):
                        if "Nome:" in linha_conta:
                            conta_nome = linha_conta.split(":")[1].strip()
                            if conta_nome == nome_conta:
                                for linha_quantia in linhas[index + 1:]:
                                    if "Quantia Inicial:" in linha_quantia:
                                        try:
                                            conta_quantia = float(linha_quantia.split(":")[1].strip())
                                            conta_origem = Conta(conta_nome, conta_quantia)
                                            break
                                        except ValueError:
                                            print("\nErro ao carregar informações da conta. Por favor, contate o suporte.\n")
                                break

                    if conta_origem:
                        for index, linha_conta_destino in enumerate(linhas):
                            if "Nome:" in linha_conta_destino:
                                conta_nome_destino = linha_conta_destino.split(":")[1].strip()
                                if conta_nome_destino == nome_conta_2:
                                    for linha_quantia_destino in linhas[index + 1:]:
                                        if "Quantia Inicial:" in linha_quantia_destino:
                                            try:
                                                conta_quantia_destino = float(linha_quantia_destino.split(":")[1].strip())
                                                conta_destino = Conta(conta_nome_destino, conta_quantia_destino)
                                                break
                                            except ValueError:
                                                print("\nErro ao carregar informações da conta de destino. Por favor, contate o suporte.\n")
                                    break

                        if conta_destino:
                            try:
                                quantia = input("Qual a quantia que pretende transferir: ")
                                conta_origem.transferencia(quantia, conta_destino)
                                print("")
                                print("*******************************************\n")
                            except ExceptionBalanco as error:
                                print(f'Transferência interrompida: {error}')
                               
                        else:
                            print(f"\nA conta com o nome '{nome_conta_2}' não foi encontrada. Por favor, tente outra vez.\n")


            except FileNotFoundError:
                print("\nEssa conta não se encontra no nosso sistema. \n")

       
            
        elif escolha == "9":
            print("\nLogout ... ")
            break

        else:
            print("\nOpção inválida. Por favor, digite um número válido!\n")

    
