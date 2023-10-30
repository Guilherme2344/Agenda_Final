import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.loginUI import LoginUI
from templates.agendahojeUI import AgendaHojeUI
from templates.manteragendaUI import ManterAgendaUI
from templates.manterservicoUI import ManterServicoUI

class IndexUI:
    def sidebar():
        st.sidebar.title('Menu')
        paginas = st.sidebar.selectbox('Selecione a página', ['Login', 'Cliente', 'Serviço', 'Agenda', 'Agenda do Dia'])
        if paginas == 'Login': LoginUI.main()
        elif paginas == 'Cliente': ManterClienteUI.main()
        elif paginas == 'Serviço': ManterServicoUI.main()
        elif paginas == 'Agenda': ManterAgendaUI.main()
        elif paginas == 'Agenda do Dia': AgendaHojeUI.main()

    def main():
        IndexUI.sidebar()

IndexUI.main()