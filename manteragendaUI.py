import streamlit as st
from view import View

class ManterAgendaUI:
    def main():
        st.header('Sistema de Agenda')
        tab_1, tab_2, tab_3, tab_4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab_1: View.agenda_listar()
        with tab_2: View.agenda_inserir()
        with tab_3: View.agenda_atualizar()
        with tab_4: View.agenda_excluir()