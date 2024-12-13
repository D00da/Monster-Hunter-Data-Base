import traceback
import psycopg2
from Monstro import Monstro
from Constantes import Constantes
from PIL import Image

# Classe que implementa o padrão Data Access Object (DAO) para a entidade pessoa
class MonstroDAO(object):

    const = Constantes()

    # Método que retorna uma lista de objetos do tipo pessoa
    def listarTodas(self):
        resultado = []
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, tipo, elemento, tamanho, nome FROM monstro order by id")
            registros = cursor.fetchall()
            for linha in registros:
                m = Monstro()
                m.id = linha[0]
                m.tipo = linha[1]
                m.elemento = linha[2]
                m.tamanho = linha[3]
                m.nome = linha[4]
                resultado.append(m)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    # Método que retorna um objeto do tipo pessoa, filtrando pelo código
    def listar_id(self, id):
        m = None
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, tipo, elemento, tamanho, nome, imagem FROM monstro WHERE id = {}".format(id))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                m = Monstro()
                m.id = linha[0]
                m.tipo = linha[1]
                m.elemento = linha[2]
                m.tamanho = linha[3]
                m.nome = linha[4]
                m.imagem = linha[5]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return m

    def listar_nome(self, nome):
        m = None
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("SELECT id, tipo, elemento, tamanho, nome, imagem FROM monstro WHERE nome = '{}'".format(nome))
            linha = cursor.fetchone()
            if linha is not None and len(linha) > 0:
                m = Monstro()
                m.id = linha[0]
                m.tipo = linha[1]
                m.elemento = linha[2]
                m.tamanho = linha[3]
                m.nome = linha[4]
                m.imagem = linha[5]
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return m


    def inserir(self, nome, elemento, tipo, tamanho, imagem):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO monstro (id, tipo, elemento, tamanho, nome, imagem) VALUES ((SELECT max(monstro.id) + 1 from monstro), '{}', '{}', '{}', '{}', '{}')".format(tipo, elemento, tamanho, nome, imagem))
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

    def atualizar(self, id, nome, elemento, tipo, tamanho, imagem):
        sucesso = False
        try:
            connection = psycopg2.connect(user=self.const.user, password=self.const.password,
                                          host=self.const.host, port=self.const.port, database=self.const.database)
            cursor = connection.cursor()
            cursor.execute("UPDATE monstro SET nome = '{}', elemento = '{}', tipo = '{}', tamanho = '{}', imagem = '{}' WHERE id = {}".format(nome, elemento, tipo, tamanho, imagem, id))
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
            cursor.execute("DELETE FROM monstro WHERE id = {}".format(id))
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