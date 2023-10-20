import streamlit as st
from view import View
from manteragendaUI import ManterAgendaUI
from manterclienteUI import ManterClienteUI
from manterservicoUI import ManterServicoUI

st.sidebar.title('Menu')
paginas = st.sidebar.selectbox('Selecione a página', ['Cliente', 'Serviço', 'Agenda'])
if paginas == 'Cliente': ManterClienteUI.main()
elif paginas == 'Serviço': ManterServicoUI.main()
elif paginas == 'Agenda': ManterAgendaUI.main()


class IndexUI:
    @classmethod
    def main(cls):
        ManterClienteUI.main()
        ManterServicoUI.main()
        ManterAgendaUI.main()


IndexUI.main()