import streamlit as st
from manterclienteUI import ManterClienteUI
from manterservicoUI import ManterServicoUI
from manteragendaUI import ManterAgendaUI
from abriragendaUI import AbrirAgendaDiaUI

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