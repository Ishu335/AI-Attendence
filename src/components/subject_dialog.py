import streamlit as st # type: ignore
from src.database.db import create_subject
from src.database.db import supabase
@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):  
    st.write("Enter the Details of new Subject")
    sub_id=st.text_input("Subjects Code :",placeholder='CS40101').upper()
    sub_name=st.text_input("Subject Name :",placeholder='English').upper()
    sub_section=st.text_input("Section :",placeholder='A').upper()


    if st.button("Create Subject Now", type="primary"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject is Created Successfully")
                st.rerun()
            except Exception as E:
                st.error(f"Error : {str(E)}")
        else:
            st.warning('Please fill all the fields')

def get_teacher_subject(teacher_id):
    response = (
        supabase.table("subjects")
        .select(
            "*, subject_students(count), attendance_logs(timestamp)"
        )
        .eq("teacher_id", teacher_id)
        .execute()
    )

    subjects = response.data

    for sub in subjects:
        # Total students
        students = sub.get("subject_students", [])
        sub["total_students"] = (
            students[0].get("count", 0) if students else 0
        )

        # Total unique attendance sessions
        attendance = sub.get("attendance_logs", [])

        unique_sessions = len(
            {
                log.get("timestamp")
                for log in attendance
                if log.get("timestamp")
            }
        )

        sub["total_classes"] = unique_sessions

        # Remove nested data
        sub.pop("subject_students", None)
        sub.pop("attendance_logs", None)

    return subjects


# def get_teacher_subject(teacher_id):
#     response = (
#         supabase.table("subjects")
#         .select(
#             "*, subject_students(count), attendance_logs(timestamp)"
#         )
#         .eq("teacher_id", teacher_id)
#         .execute()
#     )

#     subjects = response.data

#     for sub in subjects:

#         # Total students
#         sub["total_students"] = (
#             sub.get("subject_students", [{}])[0].get("count", 0)
#             if sub.get("subject_students")
#             else 0
#         )

#         # Total attendance sessions
#         attendance = sub.get("attendance_logs", [])

#         unique_sessions = len(
#             set(log["timestamp"] for log in attendance if log.get("timestamp"))
#         )

#         sub["total_classes"] = unique_sessions

#         # Remove nested data
#         sub.pop("subject_students", None)
#         sub.pop("attendance_logs", None)

#     return subjects