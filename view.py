import streamlit as st
import pandas as pd
from cliente import Cliente, NCliente

class View:
    @classmethod
    def cliente_listar(cls):
        clientes = []
        st.header('Lista de Clientes')
        for cliente in NCliente.listar():
            clientes.append(cliente.__dict__)
        dados = pd.DataFrame(clientes, columns=['Nome', 'E-mail', 'Fone'])
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