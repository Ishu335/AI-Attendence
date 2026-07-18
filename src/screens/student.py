import streamlit as st #type:ignore
from src.components.header import header_dashboard
from src.ui.base_layout import style_base_layout
from src.ui.teacher_reg import teacher_reg_style
from src.pipline.face_pipeline import predict_attendance
from  src.database.db import get_all_students,create_student
from src.pipline.face_pipeline import get_face_embeddings,train_classifier,check_face

from src.screens.student_dashboard import student_dashboard
from src.pipline.voice_pipeline import get_voice_embedding

import time
import numpy as np
from PIL import Image



def student_screen():
    style_base_layout()

    

    if 'student_data' in st.session_state :
        student_dashboard()
        st.stop()

    col1, col2 = st.columns([20,4])
    with col1:
        header_dashboard()
    with col2:
        if st.button("🏠 Home", width='stretch'):
            st.session_state["login_state"] = None
            st.rerun()
    st.markdown("""
    <style>
    [data-testid="stCameraInput"] {
        max-width: 650px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)
    st.header('Login using Face ID', text_alignment='center')
    photo_src=st.camera_input("Position yor face in the center")

    if photo_src:
        img=np.array(Image.open(photo_src))

        with st.spinner('At is Scanning...'):
            num_faces=check_face(img)
         
            if len(num_faces)==0:
                st.warning('Faces are not Found or Detected')
            elif len(num_faces) > 1:
                st.warning('Mutipal Faces are found')
            elif len(num_faces)==1:
                detected , all_ids =predict_attendance(img,num_faces) 
                if detected:
                   student_id=list(detected.keys()) [0]
                   all_students= get_all_students()
                   student=next((s for s in all_students if s['student_id']==student_id),None)
                   if student:
                       st.session_state.is_logged_in=True
                       st.session_state.user_role='student'
                       st.session_state.student_data=student
                       st.toast(f"Welcome Back {student['name']}")
                       photo_src=None
                       time.sleep(1)
                       st.rerun()   
                else:
                    st.info("Face not recognized!... You Might be new Student")
                    show_registration(img,num_faces)

def show_registration(img,num_faces):
    with st.container(border=True):
        st.header('Register New Profile')

        new_name=st.text_input('Enter Your Name',placeholder="Frist Name , Suraname Name")
        st.subheader('Optional : Voice Enrollment')
        st.info("Enroll  your for voice only attendance")

        audio_data=None

        try:
            audio_data=st.audio_input('Record a short pharase like I am Present , My name is Raj')
            # st.write(audio_data)
            # st.write(type(audio_data))

            if audio_data is not None:
                st.success("Audio received")
                time.sleep(1)
            else:
                st.error("No audio")
                time.sleep(1)
        
        except:
            st.error("Audio Data Failed")
        if st.button('Create Account ', type='primary'):
            if new_name:
                with st.spinner('Creating profile....'):
                    encodings=get_face_embeddings(img,num_faces)
                    if encodings != None:
                        face_emb=encodings[0].tolist()
                        voice_emb=None
                        if audio_data:
                            st.success("Recorded!")
                            time.sleep(1)
                            st.write(len(audio_data.getvalue()))
                            audio_bytes = audio_data.read()
                            voice_emb = get_voice_embedding(audio_bytes)
                        else:
                            st.error("Voice is Not Load")
                            time.sleep(1)
                        response_data=create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb)

                        if response_data:
                            train_classifier()
                            st.session_state.is_logged_in=True
                            st.session_state.user_role='student'
                            st.session_state.student_data=response_data[0]
                            st.toast(f'Profile Created ! Hi {new_name} ')
                            time.sleep(1)

                            st.rerun()
                    else:
                        st.error("Couldn't capture your facial  feactur or registerations")

            else:
                st.warning('Please enter your name !')
