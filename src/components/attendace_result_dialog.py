import streamlit as st #type:ignore
from src.database.db import create_attendance



# @st.dialog("Attendance Report")
def attendace_result_dialog(df,logs):
    st.write('Review Attendance Before Confirming.')
    st.dataframe(df,hide_index=True,width='stretch')


    col1, col2 = st.columns([1, 1], gap="small")
    with col1:
        if st.button("Discard",width='stretch'):
            st.session_state.voice_attendance_results=None
            st.session_state.attendace_images=[]
            st.rerun()

    with col2:
        if st.button('Confirm and Save',width='stretch',type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance Taken")
                st.session_state.attendace_images=[]
                st.session_state.voice_attendance_results=None
                st.rerun()
            except Exception as e:
                st.error('Sync failed !')

    st.markdown("""
        <style>
        div.stButton > button {
            width: 150px;
        }
        </style>
        """, unsafe_allow_html=True)
  
