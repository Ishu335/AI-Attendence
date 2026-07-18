import streamlit as st #type:ignore
from src.database.db import create_student,enroll_student_to_subject
from src.database.instance_db import supabase
import time

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the Subject Code  provided by your teacher to enroll')
    join_code=st.text_input("Subject Code", placeholder='Eg. CS1010')
    if st.button("Enroll"):
        if join_code:
            res=supabase.table('subjects').select('subject_id','name,subject_code').eq('subject_code',join_code).execute()
            if res.data:
                subject=res.data[0]
                student_id=st.session_state.student_data['student_id']
                check=supabase.table('subject_students').select('*').eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()

                if check.data:
                    st.warning('You are already enrolled in this program')

                else:
                    enroll_student_to_subject(student_id,subject['subject_id'])
                    st.success('Successfully enrolled')
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning('Plase enter a subject code')