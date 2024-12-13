from AmigatoDAO import AmigatoDAO
from time import sleep


# Classe que implementa a interface gráfica dos métodos dos caçadores
class IG_Amigato(object):

    parent = None

    # Método que imprime a tela inicial do menu de caçador
    def menu_cadastro_amigato(self):
        sleep(1)
        print("============================")
        print("Menu dos Amigatos         ")
        print("============================")
        print("1 - LISTAR")
        print("2 - INSERIR")
        print("3 - ATUALIZAR")
        print("4 - DELETAR ")
        print("0 - Voltar                  ")
        print("============================")

        opcao = input("Digite uma opção [0-4]: ")

        if opcao == '1':
            self.menu_listar_amigato()
            return
        if opcao == '2':
            self.menu_inserir_amigato()
            return
        if opcao == '3':
            self.menu_atualizar_amigato()
            return
        if opcao == '4':
            self.menu_remover_amigato()
            return
        if opcao == '0':
            print('Voltando ao Menu Inicial...')
            sleep(2)
            self.parent.menu_principal()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
            sleep(1)
            print('Voltando ao Menu dos Amigatos...')
            sleep(2)

        self.menu_cadastro_amigato()

    #Método que lista as opções de LISTAGEM de caçador
    def menu_listar_amigato(self):
        print("Abrindo Menu de Listagem...")
        sleep(2)
        print("============================")
        print("Menu Dos Amigatos         ")
        print("============================")
        print("1 - Listar Todos os Amigatos ")
        print("2 - Listar um Amigato - ID       ")
        print("3 - Listar um Amigato - NOME      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = input("Digite uma opção [0-3]: ")

        if opcao == '1':
            self.menu_listar_todos_amigatos()
            return
        if opcao == '2':
            self.menu_listar_amigato_id()
            return
        if opcao == '3':
            self.menu_listar_amigato_nome()
            return
        if opcao == '0':
            print('Voltando ao Menu Dos Amigatos...')
            sleep(2)
            self.menu_cadastro_amigato()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
        self.menu_listar_amigato()


    # Método que é chamado para listar todos os caçadores existentes
    def menu_listar_todos_amigatos(self):
        dao = AmigatoDAO()
        print("Listando Todas os Amigatos...")
        sleep(2)
        amigatos = dao.listarTodos()
        encontrou = False
        for a in amigatos:
            encontrou = True
            print('---------------------------------------------')
            print("Id = {} | Nome = {} | Nível = {} | Pelo = {} | Olhos = {} | Caçador = {}".format(a.id, a.nome, a.nivel, a.cor_pelo, a.cor_olho, a.cacador_id))
            print('---------------------------------------------')
        if not encontrou:
            print("Nenhum registro encontrado")
        sleep(2)
        self.menu_listar_amigato()

    # Método que é chamado para listar um caçador existente, filtrando pelo ID
    def menu_listar_amigato_id(self):
        dao = AmigatoDAO()
        id = int(input("Digite o ID do Amigato: "))
        a = dao.listar_id(id)
        if a is None:
            print("Nenhum registro encontrado")
        else:
            print('---------------------------------------------')
            print("Id = {} | Nome = {} | Nível = {} | Pelo = {} | Olhos = {} | Caçador = {}".format(a.id, a.nome, a.nivel, a.cor_pelo, a.cor_olho, a.cacador_id))
            print('---------------------------------------------')
        sleep(2)
        self.menu_listar_amigato()

    # Método que é chamado para listar um caçador existente, filtrando pelo NOME
    def menu_listar_amigato_nome(self):
        dao = AmigatoDAO()
        nome = input("Digite o NOME do Amigato: ")
        a = dao.listar_nome(nome)
        if a is None:
            print("Nenhum registro encontrado")
        else:
            print('---------------------------------------------')
            print("Id = {} | Nome = {} | Nível = {} | Pelo = {} | Olhos = {} | Caçador = {}".format(a.id, a.nome, a.nivel, a.cor_pelo, a.cor_olho, a.cacador_id))
            print('---------------------------------------------')
        sleep(2)
        self.menu_listar_amigato()

    # Método que é chamado para inserir um caçador existente
    def menu_inserir_amigato(self):
        dao = AmigatoDAO()
        cacador_id = input("Digite o ID do CAÇADOR do Amigato: ")
        nome = input("Digite o NOME do Amigato: ")
        nivel = input("Digite o NÍVEL do Amigato: ")
        cor_pelo = input("Digite a COR DO PELO do Amigato: ")
        cor_olho = input("Digite a COR DOS OLHOS do Amigato: ")
        sucesso = dao.inserir(nome, nivel, cor_pelo, cor_olho, cacador_id)
        if sucesso:
            print("Registro inserido com sucesso")
        else:
            print("Falha ao realizar esta operação")
        sleep(1)
        print('Voltando ao Menu dos Amigatos...')
        sleep(2)
        self.menu_cadastro_amigato()

    # Método que é chamado para atualizar um caçador existente
    def menu_atualizar_amigato(self):
        dao = AmigatoDAO()
        cacador_id = input("Digite o ID do CAÇADOR do Amigato: ")
        id = input("Digite o ID do Amigato: ")
        nome = input("Digite o NOME do Amigato: ")
        nivel = input("Digite o NÍVEL do Amigato: ")
        cor_pelo = input("Digite a COR DO PELO do Amigato: ")
        cor_olho = input("Digite a COR DOS OLHOS do Amigato: ")
        sucesso = dao.atualizar(id, nome, nivel, cor_pelo, cor_olho, cacador_id)
        if sucesso:
            print("Registro atualizado com sucesso")
        else:
            print("Falha ao realizar esta operação")
        sleep(1)
        print('Voltando ao Menu dos Amigatos...')
        sleep(2)
        self.menu_cadastro_amigato()

    # Método que lista as opções de REMOÇÃO de um caçador
    def menu_remover_amigato(self):
        print("Abrindo Menu de Remoção...")
        sleep(2)
        print("============================")
        print("Menu dos Amigatos         ")
        print("============================")
        print("1 - Remover um Amigato - ID       ")
        print("2 - Remover um Amigato - NOME      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = input("Digite uma opção [0-2]: ")

        if opcao == '1':
            self.menu_remover_amigato_id()
            return
        if opcao == '2':
            self.menu_remover_amigato_nome()
            return
        if opcao == '0':
            print('Voltando ao Menu dos Amigatos...')
            sleep(2)
            self.menu_cadastro_amigato()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
        self.menu_remover_amigato()

    # Método que é chamado para remover um caçador existente, usando o ID
    def menu_remover_amigato_id(self):
        dao = AmigatoDAO()
        id = int(input("Digite o ID do Amigato: "))
        certeza = input("Deseja realmente deletar este Amigato (S/N) ? ")
        if certeza in 'Ss':
            sucesso = dao.remover(id)
            if sucesso:
                print("Registro removido com sucesso")
            else:
                print("Falha ao realizar esta operação")
        elif certeza in 'Nn':
            print('Ação Cancelada')
        else:
            print("Falha ao realizar esta operação")
        sleep(2)
        self.menu_remover_amigato()

    # Método que é chamado para remover um caçador existente, usando o NOME
    def menu_remover_amigato_nome(self):
        dao = AmigatoDAO()
        nome = input("Digite o NOME do Amigato: ")
        certeza = input("Deseja realmente deletar este Amigato (S/N) ? ")
        if certeza in 'Ss':
            sucesso = dao.remover_nome(nome)
            if sucesso:
                print("Registro removido com sucesso")
            else:
                print("Falha ao realizar esta operação")
        elif certeza in 'Nn':
            print('Ação Cancelada')
        else:
            print("Falha ao realizar esta operação")
        sleep(2)
        self.menu_remover_amigato()



