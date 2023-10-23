import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaDiaUI

class IndexUI:
    def sidebar():
        st.sidebar.title('Menu')
        paginas = st.sidebar.selectbox('Selecione a página', ['Cliente', 'Serviço', 'Agenda', 'Agenda do Dia'])
        if paginas == 'Cliente': ManterClienteUI.main()
        elif paginas == 'Serviço': ManterServicoUI.main()
        elif paginas == 'Agenda': ManterAgendaUI.main()
        elif paginas == 'Agenda do Dia': AbrirAgendaDiaUI.main()

    def main():
        IndexUI.sidebar()

IndexUI.main()