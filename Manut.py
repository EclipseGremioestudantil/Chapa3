computadores = []
proximo_id = 1

while True: #Mantém o programa funcionando até o usuário decidir sair
    print("\n--- Menu de Manutenção de Computares ---")
    print("1.  Cadastra novo computador")
    print("2.  Listar computadores")
    print("3.  Agendar manutenção de computador")
    print("4.  Sair")
    print("---------------------------------------")

    escolha = input("Escolha uma opção: ")
    if escolha == '1': #Caso o usuário escreva "1" começará a cadastrar um dos computadores
        print("\n--- Cadastro de Computador ---")
        modelo = input("Digite o nodelo do computador: ")
        localizacao = input("Digite a localização do computador: ")
        computador = {
            "id": proximo_id,
            "modelo": modelo,
            "localizacao": localizacao,
            "status": "Operacional"
        }
        computadores.append(computador)
        print(f"Computador '{modelo}' (ID: {proximo_id}) cadastro com sucesso!")
        proximo_id += 1
    elif escolha == '2': #Caso o usuário escreva "2" começará a listar todos os computadores que cadastrou anteriormente
        print("\n--- Computadores Cadastros ---")
        if not computadores: #Caso o usuário mencione essa instância sem existir um computador cadastrado essa condição se ativará
            print("Nenhum computador cadastrado ainda.")
        else:
            for computador in computadores: #Função que faz com que uma lista apareça quando há computadores cadastrados, mostra as informações seguintes
                print(f"ID: {computador['id']}  |  "
                      f"modelo: {computador['modelo']}  |  "
                      f"localizacao: {computador['localizacao']} "
                       f"| status---------------------------")
    elif escolha =='3': #Casa o usuário esvreva 3 essa condição se ativa e começa o agendamento das manutenções
        print("\n--- Agendar Manutenção ---")
        if not computadores: #Caso não tenha nenhum computador na lista essa condição se ativa
            print("Nenhum computador para agendar manutenção. "
                  "Cadastre um primeiro.")
        else:   #Mostra os computadores da lista para serem colocados para conserto
            print("Computadores disponíveis: ")
            for computador in computadores: # Faz a lista de computadores que tem para serem consertados
                print(f"ID: {computador['id']}   |  "
                      f"Modelo: {computador['modelo']}  |  "
                      f"Status: {computador['status']}")

            id_computador_str = input("Digite o Id do computador para manutenção: ")
            if id_computador_str.isdigit(): #Verifica se tudo que foi digitado é númercaso
                id_computador = int(id_computador_str)
                encontrado = False
                for computador in computadores: #Lista as coisas do computador agendado
                    if computador["id"] == id_computador: #Verifica se o ID do computador existe
                        if computador["status"] == "Manutenção Agendada": #Verifica se o computador já está no Estado "Manutenção Agendada"
                            print(f"O computador Id {id_computador} j"
                                  f"á tem manutenção agendada.")
                        else: #Lista as coisas do computador agendado e muda o estado dele para "Manutenção Agendada"
                            computador["status"] = "Manutenção Agendada"
                            print(f"Manutenção agendada para o "
                                  f"computador ID {id_computador}.")
                        encontrado = True
                        break
                    if not encontrado: #Fala ao usuário que o ID que ele existe não foi encontrado
                        print(f"Computador com ID {id_computador} não encontrado.")
                else: #Caso o ID seja inválido informa o usuário
                    print("ID inválido. Por favor, digite um número.")
    elif escolha == '4': #Este elif garante que o código tenha um fim ao escrever 4
        print("Saindo do sistema de manutenção. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")