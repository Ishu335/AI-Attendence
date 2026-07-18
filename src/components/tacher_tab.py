from src.components.subject_dialog import create_subject_dialog,get_teacher_subject
from src.components.subject_card import subject_card
from src.components.share_subject_dialog import share_subject_dialog
from src.components.add_photos_dialog import add_photos_dialog
from src.pipline.face_pipeline import check_face,predict_attendance
from src.database.instance_db import supabase
from src.components.attendace_result_dialog import attendace_result_dialog

import streamlit as st #type: ignore
import numpy as np
from datetime import datetime
import pandas as pd

def tacher_tab_atake_attendance():
    st.header("TAKE AI ATTENDANCE")

import numpy as np

import numpy as np

def recognize_student(face_embedding, enrolled_students, threshold=0.6):
    face_embedding = np.asarray(face_embedding, dtype=np.float32).flatten()

    best_id = None
    best_distance = float("inf")

    for node in enrolled_students:
        student = node["students"]

        db_embedding = student.get("face_embedding")
        if db_embedding is None:
            continue

        db_embedding = np.asarray(db_embedding, dtype=np.float32).flatten()

        distance = np.linalg.norm(face_embedding - db_embedding)

        st.write(f"{student['student_id']} -> {distance:.4f}")

        if distance < best_distance:
            best_distance = distance
            best_id = student["student_id"]

    st.write(f"Best Distance: {best_distance:.4f}")

    if best_distance < threshold:
        return best_id

    return None


def tacher_tab_attendance_records():
    st.markdown("""
        <style>
        .stSelectbox label {
            color: white !important;
        }
        /* Main selectbox */
        .stSelectbox div[data-baseweb="select"] > div {
            background: white !important;
            color: white !important;
        }

        /* Text inside selectbox */
        .stSelectbox div[data-baseweb="select"] * {
            color: black !important;
                
        }

        /* Border */
        .stSelectbox div[data-baseweb="select"] {
            border-radius: 10px !important;
        }

        /* Dropdown menu */
        div[role="listbox"] {
            background: white !important;
        }

        div[role="option"] {
            background: white !important;
            color: black !important;
        }

        div[role="option"]:hover {
            background: white !important;
        }

        </style>
        """, unsafe_allow_html=True)
    teacher_id=st.session_state.teacher_data['teacher_id']
    st.header("ATTENDANCE RECORDS")

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images=[]

    subjects=get_teacher_subject(teacher_id)
    if not subjects:
        st.warnning("You haven't created any subject yet")
        return
    subjects_options={f"{s['name']}-{s['subject_code']}":s['subject_id'] for s in subjects}

    col1,col2=st.columns([3,1])
    with col1:
        select_subject_label=st.selectbox('Select Subject',options=list(subjects_options.keys()))
    with col2:
        if st.button('Add Photos',type='primary',icon=':material/photo_prints:',width='stretch'):
            add_photos_dialog()
    select_subject_id=subjects_options[select_subject_label]

    st.divider()

    # Photos Preview 4x4 grid
    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols=st.columns(4)

        for idex,img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idex%4]:
                st.image(img,width='stretch',caption=f'Photo{idex+1}')
        
        c1,c2,c3=st.columns(3)
        with c1:
            if st.button('Clear all photos',width='content',type='tertiary',icon=':material/delete:'):
                st.session_state.attendance_images=[]
                st.rerun()
        
        with c2:
            has_photos=bool(st.session_state.attendance_images)
            enrolled_res = (
                    supabase.table("subject_students")
                    .select("*,students(*)")
                    .eq("subject_id", select_subject_id)
                    .execute()
                )
            enrolled_students = enrolled_res.data
            # print("Enrolled Students: ",enrolled_students,"\n")

            if st.button("Run Face Analysis"):
                with st.spinner("Scanning Classroom Images..."):

                    all_detected_id = {}

                    # Analyze ALL images
                    for idx, img in enumerate(st.session_state.attendance_images):

                        img_np = np.array(img.convert("RGB"))

                        detected, _ = predict_attendance(img_np, check_face(img_np))

                        if detected:
                            for student_id in detected.keys():
                                student_id = int(student_id)
                                all_detected_id.setdefault(student_id, []).append(f"Photo {idx+1}")

                    # Fetch students AFTER processing every image
                    enrolled_res = (
                        supabase.table("subject_students")
                        .select("*,students(*)")
                        .eq("subject_id", select_subject_id)
                        .execute()
                    )

                    enrolled_students = enrolled_res.data

                    # Generate attendance
                    results = []
                    attendance_to_logs = []

                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student = node["students"]

                        sources = all_detected_id.get(int(student["student_id"]), [])

                        is_present = len(sources) > 0

                        results.append({
                            "Name": student["name"],
                            "ID": student["student_id"],
                            "Source": ", ".join(sources) if sources else "_",
                            "Status": "✔️ Present" if is_present else "❌ Absent",
                        })

                        attendance_to_logs.append({
                            "student_id": student["student_id"],
                            "subject_id": select_subject_id,
                            "timestamp": current_timestamp,
                            "is_present": is_present,
                        })

                    if results:
                        attendace_result_dialog(pd.DataFrame(results), attendance_to_logs)


                        
def tacher_tab_manage_subjects():
    teacher_id=st.session_state.teacher_data['teacher_id']
    col1,col2=st.columns(2)
    with col1:
        st.subheader('MANAGE SUBJECTS')
    with col2:
        if st.button("Create New Subject",width='content'):
            create_subject_dialog(teacher_id)
    subject=get_teacher_subject(teacher_id)

    
    if subject:
        cols=st.columns(2)
        for i, sub in enumerate(subject):
            
            stats =[
                ("👩‍🎓", "Students: ", sub['total_students']),
                ("🧑‍🏫", "Classes: ", sub ['total_classes'])
                        ]
            
            with cols[i%2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=stats
                )
                
                if st.button(f"Share Code: {sub['name']}", key=f"share_sub {i}'])", icon=":material/share:"):
                    share_subject_dialog(sub['name'], sub['subject_code'])
                    st.space()
                
    else:
        st.info("NO Subjects Found Crate One Above")
                    
