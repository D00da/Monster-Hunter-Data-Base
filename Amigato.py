class Amigato(object):

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
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def cor_pelo(self):
        return self._cor_pelo

    @cor_pelo.setter
    def cor_pelo(self, cor_pelo):
        self._cor_pelo = cor_pelo

    @property
    def cor_olho(self):
        return self._cor_olho

    @cor_olho.setter
    def cor_olho(self, cor_olho):
        self._cor_olho = cor_olho


    @property
    def cacador_id(self):
        return self._cacador_id

    @cacador_id.setter
    def cacador_id(self, cacador_id):
        self._cacador_id = cacador_id