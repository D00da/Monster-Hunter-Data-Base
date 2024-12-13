# Classe que implementa a entidade pessoa
class Monstro(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def elemento(self):
        return self._elemento

    @elemento.setter
    def elemento(self, elemento):
        self._elemento = elemento

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def imagem(self):
        return self._imagem

    @imagem.setter
    def imagem(self, imagem):
        self._imagem = imagem