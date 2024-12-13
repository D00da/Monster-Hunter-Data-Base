from PIL import Image
from MonstroDAO import MonstroDAO
from time import sleep


# Classe que implementa a interface gráfica dos métodos dos monstros
class IG_Monstro(object):

    parent = None

    def mostra_imagem(self, imagem):
        try:
            folder_path = "imagens/"
            monstro_imagem = imagem
            img = Image.open(folder_path + monstro_imagem)
            img.show()
        except:
            print("Imagem Não Encontrada")

    # Método que imprime a tela inicial do cadastro de pessoas
    def menu_cadastro_monstro(self):
        print("============================")
        print("Menu dos Monstros         ")
        print("============================")
        print("1 - LISTAR")
        print("2 - INSERIR       ")
        print("3 - ATUALIZAR      ")
        print("4 - DELETAR      ")
        print("0 - Voltar                  ")
        print("============================")

        opcao = input("Digite uma opção [0-4]: ")

        if opcao == '1':
            self.menu_listar_monstro()
            return
        if opcao == '2':
            self.menu_inserir_monstro()
            return
        if opcao == '3':
            self.menu_atualizar_monstro()
            return
        if opcao == '4':
            self.menu_deletar_monstro()
            return
        if opcao == '0':
            self.parent.menu_principal()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
            sleep(1)
            print('Voltando ao Menu dos Monstros...')
            sleep(2)

        self.menu_cadastro_monstro()


    #Método que lista as opções de LISTAGEM dos monstros
    def menu_listar_monstro(self):
        print("Abrindo Menu de Listagem...")
        sleep(2)
        print("============================")
        print("Menu dos Monstros         ")
        print("============================")
        print("1 - Listar Todos os Monstros ")
        print("2 - Listar um Monstro - ID       ")
        print("3 - Listar Monstro - NOME      ")
        print("0 - Voltar                  ")
        print("============================")
        opcao = input("Digite uma opção [0-3]: ")

        if opcao == '1':
            self.menu_listar_todos_monstros()
            return
        if opcao == '2':
            self.menu_listar_monstro_id()
            return
        if opcao == '3':
            self.menu_listar_monstro_nome()
            return
        if opcao == '0':
            print('Voltando ao Menu dos Monstros...')
            sleep(2)
            self.menu_cadastro_monstro()
            return
        else:
            print("Input Desconhecido, Digite Novamente")
        self.menu_listar_monstro()

    # Método que é chamado para listar todos os caçadores existentes
    def menu_listar_todos_monstros(self):
        dao = MonstroDAO()
        print("Listando Todos os Monstros...")
        sleep(2)
        monstros = dao.listarTodas()
        encontrou = False
        for m in monstros:
            encontrou = True
            print('---------------------------------------------')
            print("ID = {} | Nome = {} | Elemento = {} | Tipo = {} | Tamanho = {}".format(m.id, m.nome, m.elemento, m.tipo, m.tamanho))
            print('---------------------------------------------')
        if not encontrou:
            print("Nenhum registro encontrado")
        sleep(2)
        self.menu_listar_monstro()

    # Método que é chamado para listar um caçador existente, filtrando pelo ID
    def menu_listar_monstro_id(self):
        dao = MonstroDAO()
        id = int(input("Digite o ID de um monstro: "))
        m = dao.listar_id(id)
        if m is None:
            print("Nenhum registro encontrado")
        else:
            print('---------------------------------------------')
            print("ID = {} | Nome = {} | Elemento = {} | Tipo = {} | Tamanho = {}".format(m.id, m.nome, m.elemento, m.tipo, m.tamanho))
            print('---------------------------------------------')
            self.mostra_imagem(m.imagem)
        sleep(2)
        self.menu_listar_monstro()

    # Método que é chamado para listar um caçador existente, filtrando pelo NOME
    def menu_listar_monstro_nome(self):
        dao = MonstroDAO()
        nome = input("Digite o NOME de um monstro: ")
        m = dao.listar_nome(nome)
        if m is None:
            print("Nenhum registro encontrado")
        else:
            print('---------------------------------------------')
            print("ID = {} | Nome = {} | Elemento = {} | Tipo = {} | Tamanho = {}".format(m.id, m.nome, m.elemento, m.tipo, m.tamanho))
            print('---------------------------------------------')
            self.mostra_imagem(m.imagem)
        sleep(2)
        self.menu_listar_monstro()

    # Método que é chamado para inserir um caçador existente
    def menu_inserir_monstro(self):
        dao = MonstroDAO()
        nome = input("Digite o NOME do monstro: ")
        elemento = input("Digite o ELEMENTO desse monstro: ")
        tipo = input("Digite o TIPO desse monstro: ")
        tamanho = input("Digite o TAMANHO desse monstro: ")
        imagem = input("Digite a IMAGEM desse monstro: ")
        sucesso = dao.inserir(nome, elemento, tipo, tamanho, imagem)
        if sucesso:
            print("Registro inserido com sucesso!")
        else:
            print("Falha ao realizar esta operação!")
        sleep(1)
        print('Voltando ao Menu dos Monstros...')
        sleep(2)
        self.menu_cadastro_monstro()

    # Método que é chamado para atualizar um caçador existente
    def menu_atualizar_monstro(self):
        dao = MonstroDAO()
        id = int(input("Digite o ID desse monstro: "))
        nome = input("Digite o NOME do monstro: ")
        elemento = input("Digite o ELEMENTO desse monstro: ")
        tipo = input("Digite o TIPO desse monstro: ")
        tamanho = input("Digite o TAMANHO desse monstro: ")
        imagem = input("Digite a IMAGEM desse monstro: ")
        sucesso = dao.atualizar(id, nome, elemento, tipo, tamanho, imagem)
        if sucesso:
            print("Registro atualizado com sucesso")
        else:
            print("Falha ao realizar esta operação")
        sleep(1)
        print('Voltando ao Menu dos Monstros...')
        sleep(2)
        self.menu_cadastro_monstro()

    # Método que é chamado para remover um monstro existente, usando o ID
    def menu_deletar_monstro(self):
        dao = MonstroDAO()
        id = int(input("Digite o ID de um monstro: "))
        certeza = input("Deseja realmente deletar este monstro (S/N) ? ")
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
        sleep(1)
        print('Voltando ao Menu dos Monstros...')
        sleep(2)
        self.menu_cadastro_monstro()