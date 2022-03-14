from fuctions import removerRepetidos

class Arvore:
    def __init__(self, valor=' '):
        self.valor = valor
        self.no_esq = Valor()
        self.no_dir = Valor()

    def count(self, value=0):
        if (self.no_dir.esta_ocupado()):
            value = self.no_dir.count(value+1)
        if (self.no_esq.esta_ocupado()):
            value = self.no_esq.count(value+1)
        return value

    def level(self, value=0, levels = list()):
        if (self.no_dir.esta_ocupado()):
            levels.append(tuple([self.valor, value]))
            value = self.no_dir.level(value+1)[0]
        else:
            levels.append(tuple([self.valor, value]))
        if (self.no_esq.esta_ocupado()):
            levels.append(tuple([self.valor, value]))
            value = self.no_esq.level(value+1)[0]
        else:
            levels.append(tuple([self.valor, value]))
        levels = removerRepetidos(levels)
        return [value - 1, (levels)]

    def add_no(self, number):
        if number >= self.valor:
            if self.no_dir.esta_ocupado():
                self.no_dir.add_no(number)
            else:
                self.no_dir = Arvore(number)
                return
        if number < self.valor:
            if self.no_esq.esta_ocupado():
                self.no_esq.add_no(number)
            else:
                self.no_esq = Arvore(number)
                return

    def esta_ocupado(self):
        if (self.valor == ' '):
            return False
        return True


class Valor(Arvore):
    def __init__(self):
        self.valor = ' '
        self.no_dir = ' '
        self.no_esq = ' '
