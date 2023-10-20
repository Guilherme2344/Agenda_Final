class Agenda:
    def __init__(self, id, data, confirm, idCliente, idServico):
        self.__id = id
        self.__data = data
        self.__confirm = confirm
        self.__idCliente = idCliente
        self.__idServico = idServico

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_confirm(self, confirm):
        self.__confirm = confirm

    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente

    def set_idServico(self, idServico):
        self.__idServico = idServico

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_confirm(self):
        return self.__confirm

    def get_idCliente(self):
        return self.__idCliente

    def get_idServico(self):
        return self.__idServico
    
    def to_json(self):
        return { '__id' : self.__id, '__data': self.__data.strftime('%d/%m/%Y'), '__confirm': self.__confirm, '__idCliente' : self.__idCliente, '__idServico' : self.__idServico}

    def __str__(self):
        return f'{self.__id}; {self.__data}; {self.__confirm}; {self.__idCliente}; {self.__idServico}'


class NAgenda:
    __agendas = []

    @classmethod
    def inserir(cls, obj):
        NAgenda.abrir()
        id = 0
        for agenda in cls.__agendas:
            if agenda.get_id() > id: id = agenda.get_id()
        obj.set_id(id + 1)
        cls.__agendas.append(obj)
        NAgenda.salvar()

    @classmethod
    def listar(cls):
        NAgenda.abrir()
        return cls.__agendas

    @classmethod
    def listar_id(cls, id):
        NAgenda.abrir()
        for agenda in cls.__agendas:
            if agenda.get_id() == id: return agenda
        return None

    @classmethod
    def atualizar(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        if servico is not None:
            agenda.set_data(obj.get_data())
            agenda.set_confirm(obj.get_confirm())
            agenda.set_idCliente(obj.get_idCliente())
            agenda.set_idServico(obj.get_idServico())
            NAgenda.salvar()

    @classmethod
    def excluir(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        if servico is not None:
            cls.__agendas.remove(agenda)
            NAgenda.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__agendas = []
            with open('agendas.json', 'r') as arquivo:
                a = json.load(arquivo)
                for agenda in a:
                    d = Agenda(agenda['__id'], datetime.strptime(agenda['__data'], '%d/%m/%Y'), agenda['__confirm'], agenda['__idCliente'], agenda['__idServico'])
                    cls.__agendas.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('agendas.json', 'w') as arquivo:
            json.dump(cls.__agendas, arquivo, default=Agenda.to_json)
