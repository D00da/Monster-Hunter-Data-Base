# Classe que implementa a entidade pessoa
class Cacador(object):

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank
