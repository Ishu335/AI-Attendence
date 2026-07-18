import streamlit as st # type:ignore
from src.screens.home  import home_screen
from src.screens.teacher  import teacher_screen
from src.screens.student  import student_screen
from src.components.auto_enroll_dialog import auto_enroll_dialog
def main():
    if 'login_state' not in st.session_state:
        st.session_state['login_state']=None
    match st.session_state['login_state']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

    join_code = st.query_params.get("join-code")

    if join_code:
        st.session_state["pending_join_code"] = join_code

    if (
        st.session_state.get("pending_join_code")
        and st.session_state.login_state != "student"
    ):
        st.session_state.login_state = "student"
        st.rerun()
    
    # st.write("is_logged_in:", st.session_state.get("is_logged_in"))
    # st.write("user_role:", st.session_state.get("user_role"))
    # st.write("pending_join_code:", st.session_state.get("pending_join_code"))

    # if (st.session_state.get("user_role") == "student"):
    #     auto_enroll_dialog(st.session_state["pending_join_code"])


main()
# streamlit run app.py --logger.level=debug
    

# docker compose up --build