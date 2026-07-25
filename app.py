import streamlit as st # type:ignore
from src.screens.home  import home_screen
from src.screens.teacher  import teacher_screen
from src.screens.student  import student_screen

def main():
    st.set_page_config(
        page_title="VisionVoice - Smart Attendance Management System",
        page_icon="img/logo.png"
    )

    if "login_state" not in st.session_state:
        st.session_state.login_state = None

    # Check URL first
    join_code = st.query_params.get("join-code")

    if join_code:
        st.session_state.pending_join_code = join_code
        st.session_state.login_state = "student"

    match st.session_state.login_state:
        case "teacher":
            teacher_screen()
        case "student":
            student_screen(join_code)
        case _:
            home_screen()


if __name__ == "__main__":
    main()