# Dicionário para armazenar eventos e inscrições
evento = {}
inscricoes = {}

# Senha do Coordenador
coordenador_senha = "123456"

# Função para exibir o menu do aluno
def exibir_menu_aluno():
    print("________Gerenciar Eventos Universitarios - Aluno________ \n")
    print("(1) Visualizar Eventos")
    print("(2) Inscrever no Evento")
    print("(3) Voltar ao Menu Principal \n")

# Função para exibir o menu do coordenador
def exibir_menu_coordenador():
    print("________Gerenciar Eventos Universitarios - Coordenador________ \n")
    print("(1) Criar Novo Evento")
    print("(2) Atualizar Eventos")
    print("(3) Visualizar Eventos")
    print("(4) Visualizar Inscritos")
    print("(5) Cancelar Evento")
    print("(6) Excluir Eventos Cancelados")
    print("(7) Voltar ao Menu Principal \n")
    
# (1) Função para cadastrar novos eventos
def cadastrar_eventos():
    while True:
        try:
            nome_evento = input("Digite o nome do Evento: ").strip().lower()
            data_evento = input("Digite a data do Evento (dd/mm/yyyy): ").strip()
            descricao_evento = input("Digite a descrição do evento: ").strip()
            numero_participantes = int(input("Digite o número de participantes: ").strip())

            if numero_participantes <= 0:
                raise ValueError("O número de participantes deve ser um número positivo.")
            
            evento[nome_evento] = {
                "Nome Evento": nome_evento,
                "Data Evento": data_evento,
                "Descrição Evento": descricao_evento,
                "Numero Participantes": numero_participantes,
                "Inscritos": 0,
                "Status": "Ativo"
            }
            print(f"Evento '{nome_evento.title()}' cadastrado com sucesso!! \n")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        
        while True:
            try:
                continuar = input("Gostaria de cadastrar outro evento? (s/n): ").strip().lower()
                if continuar in ['s', 'n']:
                    break
                else:
                    print("Entrada inválida. Por favor, insira 's' para Sim ou 'n' para Não.")
            except ValueError:
                print("Entrada inválida. Por favor, insira 's' para Sim ou 'n' para Não.")
        
        if continuar == 'n':
            break
# Exemplo de chamada da função
# cadastrar_eventos()

# (2) Função para atualizar eventos existentes
def atualizar_eventos():
    if not evento:
        print("Sem eventos disponíveis para atualização.")
    else:
        exibir_evento()
        try:
            indice_evento = int(input("Digite o número do evento que deseja atualizar: ").strip()) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento:
                data_evento = input("Digite nova data do Evento (dd/mm/yyyy): ").strip()
                descricao_evento = input("Digite a nova descrição do evento: ").strip()
                numero_participantes = int(input("Digite o novo número de participantes: ").strip())

                if numero_participantes <= 0:
                    raise ValueError("O número de participantes deve ser um número positivo.")

                evento[nome_evento]["Data Evento"] = data_evento
                evento[nome_evento]["Descrição Evento"] = descricao_evento
                evento[nome_evento]["Numero Participantes"] = numero_participantes
                print(f"Evento '{nome_evento.title()}' atualizado com sucesso! \n")
            else:
                print("Evento não encontrado. \n")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

# Exemplo de chamada da função
# atualizar_eventos()

# (3) Função para exibir todos os eventos cadastrados
def exibir_evento():
    if not evento:
        print("Sem Evento cadastrado")  # Informa se não houver eventos cadastrados
    else:
        print("Eventos Cadastrados:\n")  # Cabeçalho da lista de eventos
        for i, (nome_evento, detalhes) in enumerate(evento.items(), start=1):
            vagas_restantes = detalhes["Numero Participantes"] - detalhes["Inscritos"]
            status = detalhes["Status"]
            print(f"{i}. Evento: {nome_evento.title()}\n"
                  f"   Data: {detalhes['Data Evento']}\n"
                  f"   Descrição: {detalhes['Descrição Evento']}\n"
                  f"   Participantes: {detalhes['Numero Participantes']}\n"
                  f"   Vagas Restantes: {vagas_restantes}\n"
                  f"   Status: {status}\n")
        print()  # Linha em branco para melhorar a legibilidade

# Exemplo de chamada da função
# exibir_evento()

# Função para obter o nome do evento pelo índice
def obter_evento_por_indice(indice):
    try:
        if 0 <= indice < len(evento):
            return list(evento.keys())[indice]
        else:
            raise IndexError("Índice fora dos limites válidos.")
    except IndexError as ie:
        print(f"Erro: {ie}")
        return None
    
# Exemplo de chamada da função
# nome_evento = obter_evento_por_indice(0)
# print(nome_evento)

# Função para inscrever um aluno no evento
def inscrever_aluno():
    while True:
        exibir_evento()
        if evento:
            try:
                indice_evento = int(input("Digite o número do evento em que deseja se inscrever: ").strip()) - 1
                nome_evento = obter_evento_por_indice(indice_evento)
                if nome_evento and evento[nome_evento]["Status"] == "Ativo":
                    if evento[nome_evento]["Inscritos"] < evento[nome_evento]["Numero Participantes"]:
                        nome_aluno = input("Digite o nome do aluno: ").strip()
                        if nome_evento in inscricoes:
                            inscricoes[nome_evento].append(nome_aluno)
                        else:
                            inscricoes[nome_evento] = [nome_aluno]
                        evento[nome_evento]["Inscritos"] += 1
                        print(f"Aluno {nome_aluno} inscrito com sucesso no evento {nome_evento}!\n")
                    else:
                        print("Não há vagas disponíveis para este evento.\n")
                else:
                    print("Evento não encontrado ou está cancelado. \n")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

        while True:
            try:
                continuar = input("Gostaria de se inscrever em outro evento? (s/n): ").strip().lower()
                if continuar in ['s', 'n']:
                    break
                else:
                    print("Entrada inválida. Por favor, insira 's' para Sim ou 'n' para Não.")
            except ValueError:
                print("Entrada inválida. Por favor, insira 's' para Sim ou 'n' para Não.")
        
        if continuar == 'n':
            break

# Exemplo de chamada da função
# inscrever_aluno()

# (4) Função para exibir inscritos em um evento e gerenciar inscrições
def exibir_inscritos():
    exibir_evento()
    if evento:
        try:
            indice_evento = int(input("Digite o número do evento para visualizar os inscritos: ").strip()) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento:
                if nome_evento in inscricoes and inscricoes[nome_evento]:
                    print(f"Inscritos no evento {nome_evento.title()}:")
                    for nome_aluno in inscricoes[nome_evento]:
                        print(f"- {nome_aluno}")
                    
                    # Opções para o coordenador gerenciar inscrições
                    while True:
                        opcao = input("Gostaria de (a) Adicionar um aluno, (b) Excluir um aluno, ou (c) Voltar ao menu? (a/b/c): ").strip().lower()
                        if opcao == 'a':
                            nome_novo_aluno = input("Digite o nome do aluno a ser adicionado: ").strip()
                            if evento[nome_evento]["Inscritos"] < evento[nome_evento]["Numero Participantes"]:
                                inscricoes[nome_evento].append(nome_novo_aluno)
                                evento[nome_evento]["Inscritos"] += 1
                                print(f"Aluno {nome_novo_aluno} adicionado com sucesso ao evento {nome_evento}!\n")
                            else:
                                print("Não há vagas disponíveis para este evento.\n")
                        elif opcao == 'b':
                            nome_aluno_excluir = input("Digite o nome do aluno a ser excluído: ").strip()
                            if nome_aluno_excluir in inscricoes[nome_evento]:
                                inscricoes[nome_evento].remove(nome_aluno_excluir)
                                evento[nome_evento]["Inscritos"] -= 1
                                print(f"Aluno {nome_aluno_excluir} excluído com sucesso do evento {nome_evento}!\n")
                            else:
                                print("Aluno não encontrado na lista de inscritos.\n")
                        elif opcao == 'c':
                            break
                        else:
                            print("Opção inválida. Por favor, escolha 'a', 'b' ou 'c'.")
                else:
                    print(f"Sem inscritos no evento {nome_evento.title()}.\n")
            else:
                print("Evento não encontrado. \n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    else:
        print("Nenhum evento disponível no momento.")

# Exemplo de chamada da função
# exibir_inscritos()

# (5) Função para cancelar eventos existentes
def cancelar_eventos():
    if not evento:
        print("Sem eventos disponíveis para cancelamento.")
    else:
        exibir_evento()
        try:
            indice_evento = int(input("Digite o número do evento que deseja cancelar: ").strip()) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento:
                confirmacao = input(f"Tem certeza que deseja cancelar o evento {nome_evento.title()}? (s/n): ").strip().lower()
                if confirmacao == 's':
                    evento[nome_evento]["Status"] = "Cancelado"  # Altera o status para cancelado
                    print(f"Evento '{nome_evento.title()}' cancelado com sucesso! \n")
                else:
                    print("Evento não cancelado. \n")
            else:
                print("Evento não encontrado. \n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# Exemplo de chamada da função
# cancelar_eventos()

# (6) Função para excluir eventos existentes
def excluir_eventos():
    if not evento:
        print("Sem eventos disponíveis para exclusão.")
        return  # Retorna imediatamente para evitar pedir confirmação duplicada
    else:
        exibir_evento()
        try:
            indice_evento = int(input("Digite o número do evento que deseja excluir: ").strip()) - 1
            nome_evento = obter_evento_por_indice(indice_evento)
            if nome_evento and "Status" in evento[nome_evento] and evento[nome_evento]["Status"] == "Cancelado":  # Verifica se o status é cancelado
                confirmacao = input(f"Tem certeza que deseja excluir o evento {nome_evento.title()}? (s/n): ").strip().lower()
                if confirmacao == 's':
                    del evento[nome_evento]
                    if nome_evento in inscricoes:
                        del inscricoes[nome_evento]
                    print(f"Evento '{nome_evento.title()}' excluído com sucesso! \n")
                else:
                    print("Exclusão de evento cancelada. \n")
            else:
                print("Evento não encontrado ou não está cancelado. \n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
            
# Exemplo de chamada da função
# excluir_eventos()

# Função para autenticar o coordenador
def autenticar_coordenador():
    senha = input("Digite a senha do coordenador: ").strip()
    if senha == coordenador_senha:
        print("Autenticação bem-sucedida! \n")
        return True
    else:
        print("Senha incorreta. \n")
        return False

# Loop principal do programa
while True:
    print("________Bem-vindo ao Gerenciador de Eventos UniFECAF________ \n")
    print("(1) Coordenador")
    print("(2) Aluno \n")

    while True:
        try:
            escolha_perfil = int(input("Você é: ").strip())
            if escolha_perfil in [1, 2]:
                break
            else:
                print("Escolha inválida. Por favor, insira 1 para Coordenador ou 2 para Aluno.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    if escolha_perfil == 1:  # Menu para Coordenador
        while not autenticar_coordenador():  # Continua solicitando senha até autenticar corretamente
            pass
        
        while True:
            exibir_menu_coordenador()
            try:
                escolha_opcao = int(input("Qual opção você deseja? ").strip())
                if escolha_opcao == 1:
                    cadastrar_eventos()
                elif escolha_opcao == 2:
                    atualizar_eventos()
                elif escolha_opcao == 3:
                    exibir_evento()
                elif escolha_opcao == 4:
                    exibir_inscritos()
                elif escolha_opcao == 5:
                    cancelar_eventos()
                elif escolha_opcao == 6:
                    excluir_eventos()
                elif escolha_opcao == 7:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
            input("Pressione Enter para voltar ao menu dos coordenadores...")

    elif escolha_perfil == 2:  # Menu para Aluno
        while True:
            exibir_menu_aluno()
            try:
                escolha_opcao = int(input("Qual opção você deseja? ").strip())
                if escolha_opcao == 1:
                    exibir_evento()
                elif escolha_opcao == 2:
                    inscrever_aluno()
                elif escolha_opcao == 3:
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
            input("Pressione Enter para voltar ao menu do aluno...")  # Confirmação unificada aqui
