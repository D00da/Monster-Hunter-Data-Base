from CacadorDAO import CacadorDAO
from time import sleep


# Classe que implementa a interface gráfica dos métodos dos caçadores
class IG_Cacador(object):

    parent = None

    # Método que imprime a tela inicial do menu de caçador
    def menu_cadastro_cacador(self):
        sleep(1)
        print("============================")
        print("Menu do Caçador         ")
        print("============================")
        print("1 - LISTAR")
        print("2 - INSERIR")
        print("3 - ATUALIZAR")
        print("4 - DELETAR ")
        print("0 - Voltar                  ")
        print("============================")

        opcao = input("Digite uma opção [0-4]: ")

        if opcao == '1':
            self.menu_listar_cacador()
            return
        if opcao == '2':
            self.menu_inserir_um_cacador()
            return
        if opcao == '3':
            self.menu_atualizar_um_cacador()
            return
        if opcao == '4':
            self.menu_remover_um_cacador()
            return
        if opcao == '0':
            print('Voltando ao Menu Inicial...')
            sleep(2)
            self.parent.menu_principal()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
            sleep(1)
            print('Voltando ao Menu do Caçador...')
            sleep(2)

        self.menu_cadastro_cacador()

    #Método que lista as opções de LISTAGEM de caçador
    def menu_listar_cacador(self):
        print("Abrindo Menu de Listagem...")
        sleep(2)
        print("============================")
        print("Menu do Caçador         ")
        print("============================")
        print("1 - Listar Todos os Caçadores ")
        print("2 - Listar um Caçador - ID      ")
        print("3 - Listar um Caçador - NOME      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = input("Digite uma opção [0-3]: ")

        if opcao == '1':
            self.menu_listar_todos_cacadores()
            return
        if opcao == '2':
            self.menu_listar_cacador_id()
            return
        if opcao == '3':
            self.menu_listar_cacador_nome()
            return
        if opcao == '0':
            print('Voltando ao Menu do Caçador...')
            sleep(2)
            self.menu_cadastro_cacador()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
        self.menu_listar_cacador()


    # Método que é chamado para listar todos os caçadores existentes
    def menu_listar_todos_cacadores(self):
        dao = CacadorDAO()
        print("Listando Todos os Caçadores...")
        sleep(2)
        cacadores = dao.listarTodos()
        encontrou = False
        for c in cacadores:
            encontrou = True
            print('---------------------------------------------')
            print("Id = {} | Nome = {} | Rank = {}".format(c.id, c.nome, c.rank))
            print('---------------------------------------------')
        if not encontrou:
            print("Nenhum registro encontrado")
        sleep(2)
        self.menu_listar_cacador()

    # Método que é chamado para listar um caçador existente, filtrando pelo ID
    def menu_listar_cacador_id(self):
        dao = CacadorDAO()
        id = int(input("Digite o ID do caçador: "))
        c = dao.listar(id)
        if c is None:
            print("Nenhum registro encontrado")
        else:
            print('---------------------------------------------')
            print("Id = {} - Nome = {} - Rank = {}".format(c.id, c.nome, c.rank))
            print('---------------------------------------------')
        sleep(2)
        self.menu_listar_cacador()

    # Método que é chamado para listar um caçador existente, filtrando pelo NOME
    def menu_listar_cacador_nome(self):
        dao = CacadorDAO()
        nome = input("Digite o NOME de um caçador: ")
        c = dao.listar_nome(nome)
        if c is None:
            print("Nenhum registro encontrado")
        else:
            print('---------------------------------------------')
            print("Id = {} - Nome = {} - Rank = {}".format(c.id, c.nome, c.rank))
            print('---------------------------------------------')
        sleep(2)
        self.menu_listar_cacador()

    # Método que é chamado para inserir um caçador existente
    def menu_inserir_um_cacador(self):
        dao = CacadorDAO()
        nome = input("Digite o NOME do caçador: ")
        rank = input("Digite o RANK desse caçador: ")
        sucesso = dao.inserir(rank, nome)
        if sucesso:
            print("Registro inserido com sucesso")
        else:
            print("Falha ao realizar esta operação")
        sleep(1)
        print('Voltando ao Menu do Caçador...')
        sleep(2)
        self.menu_cadastro_cacador()

    # Método que é chamado para atualizar um caçador existente
    def menu_atualizar_um_cacador(self):
        dao = CacadorDAO()
        id = int(input("Digite o ID desse caçador: "))
        nome = input("Digite o NOME do caçador: ")
        rank = input("Digite o RANK desse caçador: ")
        sucesso = dao.atualizar(nome, rank, id)
        if sucesso:
            print("Registro atualizado com sucesso")
        else:
            print("Falha ao realizar esta operação")
        sleep(1)
        print('Voltando ao Menu do Caçador...')
        sleep(2)
        self.menu_cadastro_cacador()

    # Método que lista as opções de REMOÇÃO de um caçador
    def menu_remover_um_cacador(self):
        print("Abrindo Menu de Remoção...")
        sleep(2)
        print("============================")
        print("Menu do Caçador         ")
        print("============================")
        print("1 - Remover um Caçador - ID       ")
        print("2 - Remover um Caçador - NOME      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = input("Digite uma opção [0-2]: ")

        if opcao == '1':
            self.menu_remover_cacador_id()
            return
        if opcao == '2':
            self.menu_remover_cacador_nome()
            return
        if opcao == '0':
            print('Voltando ao Menu do Caçador...')
            sleep(2)
            self.menu_cadastro_cacador()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
        self.menu_remover_um_cacador()

    # Método que é chamado para remover um caçador existente, usando o ID
    def menu_remover_cacador_id(self):
        dao = CacadorDAO()
        id = int(input("Digite o ID de um caçador: "))
        certeza = input("Deseja realmente deletar este usuário (S/N) ? ")
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
        self.menu_remover_um_cacador()

    # Método que é chamado para remover um caçador existente, usando o NOME
    def menu_remover_cacador_nome(self):
        dao = CacadorDAO()
        nome = input("Digite o NOME de um caçador: ")
        certeza = input("Deseja realmente deletar este usuário (S/N) ? ")
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
        self.menu_remover_um_cacador()



