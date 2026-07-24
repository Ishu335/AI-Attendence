import streamlit as st #type:ignore
from src.components.header import header_dashboard
from src.database.db import get_student_subjects,get_student_attendance,unenroll_student_to_subject
from src.components import subject_card
from src.components.enroll_dialog import enroll_dialog
from src.components.subject_card import subject_card
from src.components.auto_enroll_dialog import auto_enroll_dialog
from src.components.footer import footer_home

import time

def student_dashboard():
    
    student_data = st.session_state.student_data
    student_id=student_data['student_id']
    c1, c2 = st.columns ([8,4], vertical_alignment='center', gap='xlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state ['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1,c2=st.columns(2)
    with c1:
        st.subheader("Your Enrolled Subjects")
    with c2:
        if st.button('Enroll in Subject',type='primary',width='stretch'):
            enroll_dialog()
    
            
    st.divider()
    logs={}
    with st.spinner("Loading Your Enrolled Subjects.."):
        subjects=get_student_subjects(student_id)
        logs=get_student_attendance(student_id)


    stats_map={}
    for log in logs:
        sid=log['subject_id']
        if sid not in stats_map:
            stats_map[sid]={'total':0,'attended':0}
        stats_map[sid]['total']+=1

        if log.get('is_present'):
            stats_map[sid]['attended']+=1

    cols=st.columns(2)
    for  i ,sub_node in enumerate(subjects):
        sub=sub_node['subjects']
        sid=sub['subject_id']
        stats=stats_map.get(sid,{'total':0,
                                 'attended':0})
        
        def unenroll_btn():
            if st.button("Unenroll This Course",width='content', key=f"unenroll_{sid}"):
                unenroll_student_to_subject(student_id,sid)
                st.toast('Unenroll Successfully')
                time.sleep(0.7)
                st.rerun()

                
        with cols[i%2]:
            subject_card(name=sub['name'],
                         code=sub['subject_code'],
                         section=sub['section'],
                         stats=[
                             ('🗓️','Total',stats['total']),
                             ('✔️','Attended',stats['attended']),
                         ],
                        footer_callback=unenroll_btn)
    footer_home()