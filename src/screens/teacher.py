import streamlit as st # type:ignore
from src.components.header import header_dashboard
from src.ui.base_layout import style_base_layout
from src.ui.teacher_reg import teacher_reg_style
from src.database.db import teacher_register,check_teacher_username,teacher_login
from src.screens.teacher_dashboard import teacher_dashboard_fun




def teacher_screen():
    style_base_layout()
    teacher_reg_style()

    if 'teacher_data' in st.session_state:
        teacher_dashboard_fun()

    else:
        col1, col2 = st.columns([20,4])
        with col1:
            header_dashboard()

        with col2:
            if st.button("🏠 Home", width='stretch'):
                st.session_state["login_state"] = None
                st.rerun()

        if (
            'teacher_login_type' not in st.session_state
            or st.session_state.teacher_login_type == "login"
        ):
            teacher_login_screen()

        elif st.session_state.teacher_login_type == "register":
            teacher_register_screen()



def login_check(username,password):
    if not username:
        st.error("Enter the Username")
        return False
    elif not password:
        st.error("Enter the Password")
        return False
    teacher= teacher_login(username,password)
    if teacher:
        st.session_state.user_role='teacher'
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True
    return False
def register_check(username,name,password,confirm_password):
    if not username:
        return False,'Username is Missing'
    elif not name:
        return False,'Name is Missing'
    elif not  password:
        return False,'Password is Missing'
    elif not confirm_password or confirm_password!=password:
        return False,'Password and Confirm Password not matched'
    if check_teacher_username(username):
        return False,'Username already existing'
    try:
        teacher_register(username,password,name)
        return True,"Sucessfuly Created Login Now"
    except Exception as e:
        return False,"Unexpected Error!"
    
def teacher_register_screen():
    st.header("Register your Teacher Profile")
    username = st.text_input("Username",placeholder="abhishek")
    name = st.text_input("Full Name",placeholder="Abhishek Sharma")
    password = st.text_input("Password",type="password")

    confirm_password = st.text_input("Confirm Password", type="password")

    col1, col2 = st.columns(2,gap="large")
    with col1:
        if st.button("👨‍🏫 Register Now",width='stretch'):
            success,message=register_check(username,name,password,confirm_password)
            if success:
                st.toast(message)
                import time as t 
                t.sleep(2)
                st.session_state.teacher_login_type="login"
                st.rerun()
            else:
                st.error(message)
    with col2:
        if st.button("🔑 Login Instead",width='stretch'):
            st.session_state.teacher_login_type="login"
            st.rerun()



def teacher_login_screen():
    st.header("Login to your Teacher Profile")

    username = st.text_input("Username",placeholder="Example")
    password = st.text_input("Password",placeholder="Example@123",type="password")

    col1, col2 = st.columns(2,gap="large")
    with col1:
            if st.button("🔑 Login Instead",width='stretch'):
                if login_check(username,password):
                    st.toast("Welcome Teacher")
                    import time
                    time.sleep(2)
                    st.rerun()
                else:
                    st.toast("User not exist")
            
    with col2:
        if st.button("👨‍🏫 Register Now",width='stretch'):
                st.session_state.teacher_login_type="register"
                st.rerun()
    
    