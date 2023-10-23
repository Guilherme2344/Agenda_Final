import streamlit as st
import pandas as pd
from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import time
from datetime import datetime, timedelta

class View:
    @classmethod
    def cliente_listar(cls):
        clientes = []
        st.header('Lista de Clientes')
        for cliente in NCliente.listar():
            clientes.append([cliente.get_id(), cliente.get_nome(), cliente.get_email(), cliente.get_fone()])
        dados = pd.DataFrame(clientes, columns=['Id', 'Nome', 'E-mail', 'Fone'])
        st.dataframe(dados, hide_index=True)

    @classmethod
    def cliente_inserir(cls):
        st.header('Inserir Cliente')
        with st.form('inserir'):
            nome = st.text_input('Nome')
            email = st.text_input('E-mail')
            fone = st.text_input('Fone')
            if st.form_submit_button('Inserir'):
                cliente = Cliente(0, nome, email, fone)
                NCliente.inserir(cliente)
                st.success('Cliente inserido com sucesso!')
                time.sleep(1.5)
                st.rerun()

    @classmethod
    def cliente_atualizar(cls):
        clientes = []
        for cliente in NCliente.listar(): 
            clientes.append(cliente)
        st.header('Atualizar Cliente')
        with st.form('atualizar'):
            opcao = st.selectbox('Qual cliente você quer atualizar?', (clientes), index=None, placeholder='Selecione o cliente')
            nome = st.text_input('Novo nome')
            email = st.text_input('Novo e-mail')
            fone = st.text_input('Novo fone')
            if st.form_submit_button('Atualizar'):
                cliente = Cliente(opcao.get_id(), nome, email, fone)
                NCliente.atualizar(cliente)
                st.success('Cliente atualizado com sucesso!')
                time.sleep(1.5)
                st.rerun()

    @classmethod
    def cliente_excluir(cls):
        clientes = []
        for cliente in NCliente.listar(): 
            clientes.append(cliente)
        st.header('Excluir Cliente')
        with st.form('excluir'):
            opcao = st.selectbox('Qual cliente você quer excluir?', (clientes), index=None, placeholder='Selecione o cliente')
            if st.form_submit_button('Excluir'):
                cliente = Cliente(opcao.get_id(), '', '', '')
                NCliente.excluir(cliente)
                st.success('Cliente excluído com sucesso!')
                time.sleep(1.5)
                st.rerun()

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
                st.success('Serviço inserido com sucesso!')
                time.sleep(1.5)
                st.rerun()

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
                st.success('Serviço atualizado com sucesso!')
                time.sleep(1.5)
                st.rerun()

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
                st.success('Serviço excluído com sucesso!')
                time.sleep(1.5)
                st.rerun()

    @classmethod
    def agenda_listar(cls):
        agendas = []
        st.header('Lista de Agendas')
        for agenda in NAgenda.listar():
            agendas.append([agenda.get_id(), agenda.get_data(), agenda.get_confirm(), agenda.get_idCliente(), agenda.get_idServico()])
        dados = pd.DataFrame(agendas, columns=['ID', 'Data', 'Confirmado', 'ID_Cliente', 'ID_Serviço'])
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
            idcliente = st.selectbox('Cliente', (clientes), index=None, placeholder='Selecione o cliente')
            idservico = st.selectbox('Serviço', (servicos), index=None, placeholder='Selecione o serviço')
            if st.form_submit_button('Inserir'):
                agenda = Agenda(0, data, confirm, idcliente.get_id(), idservico.get_id())
                NAgenda.inserir(agenda)
                st.success('Agenda inserida com sucesso')
                time.sleep(1.5)
                st.rerun()

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
                agenda = Agenda(op.get_id(), data, confirm, idcliente.get_id(), idservico.get_id())
                NAgenda.atualizar(agenda)
                st.success('Agenda atualizada com sucesso!')
                time.sleep(1.5)
                st.rerun()

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
                st.success('Agenda excluída com sucesso!')
                time.sleep(1.5)
                st.rerun()

    @classmethod
    def agenda_abrir_dia(cls):
        st.header('Abrir Agenda do Dia')
        with st.form('abrir'):
            data = st.date_input('Data', format='DD/MM/YYYY')
            tempo_init = st.text_input('Primeiro horário')
            tempo_end = st.text_input('Último horário')
            duracao = st.text_input('Duração do Serviço')
            if st.form_submit_button('Inserir Horários'):
                tempo_init_format = datetime.strptime(tempo_init, '%H:%M')
                tempo_final_format = datetime.strptime(tempo_end, '%H:%M')
                duracao_format = datetime.strptime(duracao, '%M')
                while tempo_init_format <= tempo_final_format:
                    data_horario_format = datetime(data.year, data.month, data.day, tempo_init_format.hour, tempo_init_format.minute)
                    agenda = Agenda(0, data_horario_format, 0, 0, 0)
                    NAgenda.inserir(agenda)
                    tempo_init_format += timedelta(minutes=duracao_format.minute)
                st.success('Horários inseridos com sucesso!')
                time.sleep(1.5)
                st.rerun()