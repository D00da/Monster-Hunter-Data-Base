import traceback
import psycopg2
from Cacador import Cacador
from Constantes import Constantes

# Classe que implementa o padrão Data Access Object (DAO) para a entidade pessoa
class CacadorDAO(object):

    const = Constantes()

    # Método que retorna uma lista de objetos do tipo pessoa
    def listarTodos(self):
        resultado = []
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, rank, nome FROM cacador order by id")
            registros = cursor.fetchall()
            for linha in registros:
                c = Cacador()
                c.id = linha[0]
                c.rank = linha[1]
                c.nome = linha[2]
                resultado.append(c)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # Método que retorna um objeto do tipo pessoa, filtrando pelo código
    def listar(self, id):
        c = None
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, rank, nome FROM cacador WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                c = Cacador()
                c.id = linha[0]
                c.rank = linha[1]
                c.nome = linha[2]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    def listar_nome(self, nome):
        c = None
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, rank, nome FROM cacador WHERE nome = '{}'".format(nome))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                c = Cacador()
                c.id = linha[0]
                c.rank = linha[1]
                c.nome = linha[2]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return c

    # Método utilizado para inserir uma nova pessoa
    def inserir(self, rank, nome):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO cacador (id, rank, nome) VALUES ((select max(cacador.id) + 1 from cacador), '{}', '{}')".format(rank, nome))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # Método utilizado para atualizar os dados de nome, login e senha de uma pessoa existente
    def atualizar(self, nome, rank, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE cacador SET nome = '{}', rank = '{}' WHERE id = {}".format(nome, rank, id))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    # Método utilizado para remover uma pessoa existente
    def remover(self, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cacador WHERE id = {}".format(id))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso

    def remover_nome(self, nome):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cacador WHERE nome = '{}'".format(nome))
            connection.commit()
            if cursor.rowcount == 1:
                sucesso = True
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucesso