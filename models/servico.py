import json

class Servico:
    def __init__(self, id, desc, valor, duracao):
        self.__id = id
        self.__desc = desc
        self.__valor = valor
        self.__duracao = duracao

    def set_id(self, id):
        self.__id = id

    def set_desc(self, desc):
        self.__desc = desc

    def set_valor(self, valor):
        self.__valor = valor

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def get_id(self):
        return self.__id

    def get_desc(self):
        return self.__desc

    def get_valor(self):
        return self.__valor

    def get_duracao(self):
        return self.__duracao

    def __str__(self):
        return f'{self.__id}; {self.__desc}; {self.__valor}; {self.__duracao}'


class NServico:
    __servicos = []
    
    @classmethod
    def inserir(cls, servico):
        NServico.abrir()
        id = 0
        for i in cls.__servicos:
            if i.get_id() > id: id = i.get_id()
        servico.set_id(id + 1)
        cls.__servicos.append(servico)
        NServico.salvar()

    @classmethod
    def listar(cls):
        NServico.abrir()
        return cls.__servicos

    @classmethod
    def listar_id(cls, id):
        NServico.abrir()
        for i in cls.__servicos:
            if i.get_id() == id: return i
        return None

    @classmethod
    def atualizar(cls, obj):
        NServico.abrir()
        servico = NServico.listar_id(obj.get_id())
        if servico is not None:
            servico.set_desc(obj.get_desc())
            servico.set_valor(obj.get_valor())
            servico.set_duracao(obj.get_duracao())
            NServico.salvar()

    @classmethod
    def excluir(cls, obj):
        NServico.abrir()
        servico = NServico.listar_id(obj.get_id())
        if servico is not None:
            cls.__servicos.remove(servico)
            NServico.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__servicos = []
            with open('servicos.json', 'r') as arquivo:
                a = json.load(arquivo)
                for servico in a:
                    s = Servico(servico['_Servico__id'], servico['_Servico__desc'], servico['_Servico__valor'], servico['_Servico__duracao'])
                    cls.__servicos.append(s)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('servicos.json', 'w') as arquivo:
            json.dump(cls.__servicos, arquivo, default=vars)
