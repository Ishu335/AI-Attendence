import streamlit as st #type:ignore
from PIL import Image
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_backgroud_home, style_base_layout
from src.ui.home_style import home_style_page

if 'login_state' not in st.session_state:
    st.session_state['login_state'] = None


def home_screen():

    style_base_layout()
    style_backgroud_home()
    header_home()
    home_style_page()
    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("I'm Teacher")
        st.image("img/teacher.jpg", width=350)
        if st.button("Teacher Portal",icon=":material/arrow_outward:",icon_position='right'):
            st.session_state['login_state']='teacher'
            st.rerun()
    
    @st.cache_data
    def load_image():
        return Image.open("img/student.jpg")

    with col2:
        st.header("I'm Student")
        st.image(load_image(), width=350)
        if st.button("Student Portal",icon=":material/arrow_outward:",icon_position="right"):
            st.session_state['login_state'] = 'student'
            st.rerun()
    footer_home()