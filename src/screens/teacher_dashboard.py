import streamlit as st #type:ignore
from src.components.header import header_dashboard
from src.components.tacher_tab import tacher_tab_atake_attendance,tacher_tab_attendance_records,tacher_tab_manage_subjects
from src.ui.base_layout import  style_base_layout

# style_base_layout()
def teacher_dashboard_fun():
    teacher_data = st.session_state.teacher_data
    c1, c2 = st.columns ([8,4], vertical_alignment='center', gap='xlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state ['is_logged_in'] = False
            del st.session_state.teacher_data
            st.rerun()
            st.space()


    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1, tab2, tab3 = st.columns([1, 1, 1])
    st.markdown("""
        <style>
        div.stButton > button {
            width: 202px;
        }
        </style>
        """, unsafe_allow_html=True)
    with tab1:
        type1='primary' if st.session_state.current_teacher_tab == 'take_attendance' else 'tertiary' 
        if st.button('Take Attendance', type=type1,icon= ':material/ar_on_you:'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2='primary' if st.session_state.current_teacher_tab == 'manage_subjects' else 'tertiary' 
        if st.button('Manage Subjects',  type=type2, icon= ':material/book_ribbon:'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()
    with tab3:
        type3='primary' if st.session_state.current_teacher_tab == 'attendance_records' else 'tertiary' 
        if st.button('Attendance Records',   type=type3,icon= ':material/cards_stack:'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    if  st.session_state.current_teacher_tab == 'attendance_records':
        tacher_tab_attendance_records()
    elif  st.session_state.current_teacher_tab == 'manage_subjects':
        tacher_tab_manage_subjects()
    elif st.session_state.current_teacher_tab == 'take_attendance' :
        tacher_tab_atake_attendance()
