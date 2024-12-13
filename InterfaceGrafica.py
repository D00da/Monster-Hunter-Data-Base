from IG_Cacador import IG_Cacador
from IG_Monstro import IG_Monstro
from IG_Amigato import IG_Amigato
from time import sleep

# Classe que implementa a interface gráfica de toda a aplicação
class InterfaceGrafica(object):

    # Método que imprime a tela inicial da aplicação
    def menu_principal(self):

        cacador = IG_Cacador()
        cacador.parent = self

        monstro = IG_Monstro()
        monstro.parent = self

        amigato = IG_Amigato()
        amigato.parent = self

        print('============================================================================')
        print('============================================================================')
        print('___  ____ _  _ ____ ____    ___  ____    ___  ____ ___  ____ ____')
        print('|__] |__| |\ | |    |  |    |  \ |___    |  \ |__| |  \ |  | [__  .')
        print('|__] |  | | \| |___ |__|    |__/ |___    |__/ |  | |__/ |__| ___] .')
        print('')
        print('                               ------')
        print('  __  __                 _              _   _             _')
        print(' |  \/  | ___  _ __  ___| |_ ___ _ __  | | | |_   _ _ __ | |_ ___ _ __')
        print(" | |\/| |/ _ \| '_ \/ __| __/ _ \ '__| | |_| | | | | '_ \| __/ _ \ '__|")
        print(' | |  | | (_) | | | \__ \ ||  __/ |    |  _  | |_| | | | | ||  __/ |')
        print(' |_|  |_|\___/|_| |_|___/\__\___|_|    |_| |_|\__,_|_| |_|\__\___|_|')
        print('')
        print('============================================================================')
        print("Carregando Banco...")
        sleep(2)
        print('============================================================================')
        print("1 - Cadastro de Caçador ")
        print("2 - Cadastro de Monstro ")
        print("3 - Cadastro de Amigato ")
        print("0 - Sair")
        print("========================")

        opcao = input("Digite uma opção [0-3]: ")

        if opcao == '1':
            print('Abrindo Menu do Caçador...')
            sleep(1)
            cacador.menu_cadastro_cacador()
            return

        elif opcao == '2':
            print('Abrindo Menu dos Monstros...')
            sleep(1)
            monstro.menu_cadastro_monstro()
            return

        elif opcao == '3':
            print('Abrindo Menu dos Amigatos...')
            sleep(1)
            amigato.menu_cadastro_amigato()
            return

        elif opcao == '0':
            return

        else:
            print("Input Desconhecido, Digite Novamente")
            sleep(1)
            print('Voltando ao Menu Inicial...')
            sleep(2)

        self.menu_principal()


# Inicializa a aplicação
if __name__ == '__main__':
    gui = InterfaceGrafica()
    gui.menu_principal()