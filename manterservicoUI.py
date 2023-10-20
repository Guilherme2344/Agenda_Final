import streamlit as st
from view import View

class ManterServicoUI:
    def main():
        st.header('Sistema de Agenda')
        tab_1, tab_2, tab_3, tab_4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab_1: View.servico_listar()
        with tab_2: View.servico_inserir()
        with tab_3: View.servico_atualizar()
        with tab_4: View.servico_excluir()