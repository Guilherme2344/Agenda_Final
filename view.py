import streamlit as st
import pandas as pd
from models.agenda import Agenda, NAgenda
from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
import time
from datetime import datetime, timedelta

class View:
    @classmethod
    def cliente_listar(cls):
        st.header('Lista de Clientes')
        clientes = []
        for cliente in NCliente.listar():
            clientes.append([cliente.get_id(), cliente.get_nome(), cliente.get_email(), cliente.get_fone()])
        if len(clientes) == 0:
            st.write('Nenhum cliente cadastrado')
        else:
            dados = pd.DataFrame(clientes, columns=['Id', 'Nome', 'E-mail', 'Fone'])
            st.dataframe(dados, hide_index=True)

    @classmethod
    def cliente_inserir(cls):
        st.header('Abrir Conta')
        with st.form('abrir', clear_on_submit=True):
            nome = st.text_input('Nome')
            email = st.text_input('E-mail')
            fone = st.text_input('Fone')
            senha = st.text_input('Senha')
            if st.form_submit_button('Criar'):
                cliente = Cliente(0, nome, email, fone, senha)
                NCliente.inserir(cliente)


    @classmethod
    def cliente_atualizar(cls):
        clientes = []
        for cliente in NCliente.listar(): 
            clientes.append(cliente)
        st.header('Atualizar Cliente')
        if len(clientes) == 0:
            st.write('Nenhum cliente cadastrado')
        else:
            with st.form('atualizar', clear_on_submit=True):
                opcao = st.selectbox('Qual cliente você quer atualizar?', (clientes), index=None, placeholder='Selecione o cliente')
                nome = st.text_input('Novo nome')
                email = st.text_input('Novo e-mail')
                fone = st.text_input('Novo fone')
                senha = st.text_input('Nova senha')
                if st.form_submit_button('Atualizar'):
                    cliente = Cliente(opcao.get_id(), nome, email, fone, senha)
                    NCliente.atualizar(cliente)

    @classmethod
    def cliente_excluir(cls):
        clientes = []
        for cliente in NCliente.listar(): 
            clientes.append(cliente)
        st.header('Excluir Cliente')
        if len(clientes) == 0:
            st.write('Nenhum cliente cadastrado')
        else:
            with st.form('excluir'):
                opcao = st.selectbox('Qual cliente você quer excluir?', (clientes), index=None, placeholder='Selecione o cliente')
                if st.form_submit_button('Excluir'):
                    cliente = Cliente(opcao.get_id(), '', '', '', '')
                    NCliente.excluir(cliente)

    @classmethod
    def cliente_login(cls):
        st.header('Login')
        with st.form('login', clear_on_submit=True):
            email = st.text_input('E-mail')
            senha = st.text_input('Senha')
            if st.form_submit_button('Login'):
                lista_1 = []
                lista_2 = []
                for cliente in NCliente.listar():
                    lista_1.append(cliente.get_email())
                    lista_2.append(cliente.get_senha())
                if email in lista_1 and senha in lista_2:
                    st.success('Login realizado com sucesso')
                else:
                    st.error('Usuário ou senha inválido(s)')

    @classmethod
    def servico_listar(cls):
        servicos = []
        st.header('Lista de Serviços')
        for servico in NServico.listar():
            servicos.append([servico.get_id(), servico.get_desc(), servico.get_valor(), servico.get_duracao()])
        dados = pd.DataFrame(servicos, columns=['ID', 'Descrição', 'Valor', 'Duração'])
        st.dataframe(dados, hide_index=True)

    @classmethod
    def servico_inserir(cls):
        st.header('Inserir Serviços')
        with st.form('inserir'):
            desc = st.text_input('Descrição')
            valor = st.number_input('Valor')
            duracao = st.text_input('Duração')
            if st.form_submit_button('Inserir'):
                servico = Servico(0, desc, valor, duracao)
                NServico.inserir(servico)

    @classmethod
    def servico_atualizar(cls):
        servicos = []
        for servico in NServico.listar(): 
            servicos.append(servico)
        st.header('Atualizar Serviços')
        with st.form('atualizar'):
            op = st.selectbox('Qual serviço você quer atualizar?', (servicos), index=None, placeholder='Selecione o serviço')
            desc = st.text_input('Nova descrição')
            valor = st.number_input('Novo valor')
            duracao = st.text_input('Nova duração')
            if st.form_submit_button('Atualizar'):
                servico = Servico(op.get_id(), desc, valor, duracao)
                NServico.atualizar(servico)

    @classmethod
    def servico_excluir(cls):
        servicos = []
        for servico in NServico.listar(): 
            servicos.append(servico)
        st.header('Excluir Serviço')
        with st.form('excluir'):
            op = st.selectbox('Qual servico você quer excluir?', (servicos), index=None, placeholder='Selecione o serviço')
            if st.form_submit_button('Excluir'):
                servico = Servico(op.get_id(), '', '', '')
                NServico.excluir(servico)

    @classmethod
    def agenda_listar_hoje(cls):
        st.header('Agenda de Hoje')
        lista = []
        hoje = datetime.today()
        for agenda in NAgenda.listar():
            if agenda.get_data() == hoje and agenda.get_confirm() == False:
                lista.append([agenda.get_id(), agenda.get_data(), agenda.get_confirm(), agenda.get_idCliente(), agenda.get_idServico()])
        dados = pd.DataFrame(agendas, columns=['ID', 'Data', 'Confirmado', 'Cliente', 'Serviço'])
        st.dataframe(dados)
        
    @classmethod
    def agenda_listar(cls):
        agendas = []
        st.header('Lista de Agendas')
        for agenda in NAgenda.listar():
            agendas.append([agenda.get_id(), agenda.get_data(), agenda.get_confirm(), agenda.get_idCliente(), agenda.get_idServico()])
        dados = pd.DataFrame(agendas, columns=['ID', 'Data', 'Confirmado', 'Cliente', 'Serviço'])
        st.dataframe(dados, hide_index=True)

    @classmethod
    def agenda_inserir(cls):
        clientes = []
        servicos = []
        for cliente in NCliente.listar(): 
            clientes.append(cliente)
        for servico in NServico.listar():
            servicos.append(servico)
        st.header('Inserir Agenda')
        with st.form('inserir'):
            data = st.date_input('Data', format='DD/MM/YYYY')
            confirm = st.checkbox('Confirmado?', value=False)
            if confirm == False: confirm = False
            else: confirm = True
            idcliente = st.selectbox('Cliente', (clientes), index=None, placeholder='Selecione o cliente')
            idservico = st.selectbox('Serviço', (servicos), index=None, placeholder='Selecione o serviço')
            if st.form_submit_button('Inserir'):
                agenda = Agenda(0, data, confirm, idcliente.get_nome(), idservico.get_desc())
                NAgenda.inserir(agenda)

    @classmethod
    def agenda_atualizar(cls):
        agendas = []
        clientes = []
        servicos = []
        for agenda in NAgenda.listar(): 
            agendas.append(agenda)
        for cliente in NCliente.listar(): 
            clientes.append(cliente)
        for servico in NServico.listar():
            servicos.append(servico)
        st.header('Atualizar Agenda')
        with st.form('atualizar'):
            op = st.selectbox('Qual agenda você quer atualizar?', (agendas), index=None, placeholder='Selecione a agenda')
            data = st.date_input('Nova data', format='DD/MM/YYYY')
            confirm = st.checkbox('Confirmado?', value=False)
            idcliente = st.selectbox('Novo cliente', (clientes), index=None, placeholder='Selecione o cliente')
            idservico = st.selectbox('Novo serviço', (servicos), index=None, placeholder='Selecione o serviço')
            if st.form_submit_button('Atualizar'):
                agenda = Agenda(op.get_id(), data, confirm, idcliente.get_nome(), idservico.get_desc())
                NAgenda.atualizar(agenda)

    @classmethod
    def agenda_excluir(cls):
        agendas = []
        for agenda in NAgenda.listar(): 
            agendas.append(agenda)
        st.header('Excluir Agenda')
        with st.form('excluir'):
            op = st.selectbox('Qual agenda você quer excluir?', (agendas), index=None, placeholder='Selecione a agenda')
            if st.form_submit_button('Excluir'):
                agenda = Agenda(op.get_id(), '', '', '', '')
                NAgenda.excluir(agenda)
