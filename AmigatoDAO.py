import traceback
import psycopg2
from Amigato import Amigato
from Constantes import Constantes

# Classe que implementa o padrão Data Access Object (DAO) para a entidade pessoa
class AmigatoDAO(object):

    const = Constantes()

    # Método que retorna uma lista de objetos do tipo pessoa
    def listarTodos(self):
        resultado = []
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, nivel, cor_pelo, cor_olho, cacador_id nome FROM amigato order by id")
            registros = cursor.fetchall()
            for linha in registros:
                a = Amigato()
                a.id = linha[0]
                a.nome = linha[1]
                a.nivel = linha[2]
                a.cor_pelo = linha[3]
                a.cor_olho = linha[4]
                a.cacador_id = linha[5]
                resultado.append(a)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # Método que retorna um objeto do tipo pessoa, filtrando pelo código
    def listar_id(self, id):
        a = None
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, nivel, cor_pelo, cor_olho, cacador_id FROM amigato WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                a = Amigato()
                a.id = linha[0]
                a.nome = linha[1]
                a.nivel = linha[2]
                a.cor_pelo = linha[3]
                a.cor_olho = linha[4]
                a.cacador_id = linha[5]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return a

    def listar_nome(self, nome):
        a = None
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, nivel, cor_pelo, cor_olho, cacador_id FROM amigato WHERE nome = '{}'".format(nome))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                a = Amigato()
                a.id = linha[0]
                a.nome = linha[1]
                a.nivel = linha[2]
                a.cor_pelo = linha[3]
                a.cor_olho = linha[4]
                a.cacador_id = linha[5]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return a


    def inserir(self, nome, nivel, cor_pelo, cor_olho, cacador_id):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO amigato (id, nome, nivel, cor_pelo, cor_olho, cacador_id) VALUES ((SELECT max(amigato.id) + 1 from amigato), '{}', '{}', '{}', '{}', '{}')".format(nome, nivel, cor_pelo, cor_olho, cacador_id))
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

    def atualizar(self, id, nome, nivel, cor_pelo, cor_olho, cacador_id):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE amigato SET nome = '{}', nivel = '{}', cor_pelo = '{}', cor_olho = '{}', cacador_id = '{}' WHERE id = {}".format(nome, nivel, cor_pelo, cor_olho, cacador_id, id))
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

    def remover(self, id):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM amigato WHERE id = {}".format(id))
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
            cursor.execute("DELETE FROM amigato WHERE nome = '{}'".format(nome))
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