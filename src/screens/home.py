import streamlit as st #type:ignore
from PIL import Image
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_backgroud_home, style_base_layout
import base64

if 'login_state' not in st.session_state:
    st.session_state['login_state'] = None


def home_screen():

    style_base_layout()
    style_backgroud_home()
    header_home()
    col1, col2 = st.columns(2,gap="large")
    def get_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    
    with col1:
        st.markdown("""
               <style>
               .teacher{
                   font-size:1.8rem;
                   font-weight:800;
                   color:orange;
                   text-align:center;
                   width:fit-content;
                   margin-top:-40px;      
                   margin-bottom:25px;    
                   margin-left:auto;
                   margin-right:auto;
               }
               </style>
               """, unsafe_allow_html=True)
       
        st.markdown(
            '<div class="teacher">I\'m Teacher</div>',
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown(f"""
            <div style="
                display:flex;
                justify-content:center;
                margin-top:-40px;
            ">
                <img src="data:image/png;base64,{get_base64("img/teacher.png")}"
                    width="350"
                    style="
                        filter: drop-shadow(60px 12px 25px rgba(0,0,0,0.30));
                    ">
            </div>
            """, unsafe_allow_html=True)
        st.write("")
        # if st.button("Teacher Portal",icon=":material/arrow_outward:",icon_position='right'):
        if st.button("Teacher Portal",icon=":material/arrow_outward:"):
            st.session_state['login_state']='teacher'
            st.rerun()
    
    with col2:
        st.markdown("""
                       <style>
                       .teacher{
                           font-size:1.8rem;
                           font-weight:800;
                           color:orange;
                           text-align:center;
                           width:fit-content;
                           margin-top:-40px;      
                           margin-bottom:25px;    
                           margin-left:auto;
                           margin-right:auto;
                           
                       }
                       </style>
                       """, unsafe_allow_html=True)
               
        st.markdown(
            '<div class="teacher">I\'m Student</div>',
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown(f"""
                    <div style="
                        display:flex;
                        justify-content:center;
                        margin-top:-40px;
                    ">
                        <img src="data:image/png;base64,{get_base64("img/student.png")}"
                            width="350"
                            style="
                                filter: drop-shadow(40px 12px 25px rgba(0,0,0,0.28));
                            ">
                    </div>
                    """, unsafe_allow_html=True)
        st.write('')
        if st.button("Student Portal",icon=":material/arrow_outward:"):
            st.session_state['login_state'] = 'student'
            st.rerun()
    footer_home()