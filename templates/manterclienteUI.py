import streamlit as st
from view import View

class ManterClienteUI:
    def main():
        st.header('OBS: o rerun está bugando. Toda vez que executar uma operação, recarregue a página pressionando a tecla R')
        st.header('Sistema de Cliente')
        tab_1, tab_2, tab_3, tab_4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab_1: View.cliente_listar()
        with tab_2: View.cliente_inserir()
        with tab_3: View.cliente_atualizar()
        with tab_4: View.cliente_excluir()
