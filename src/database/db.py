from  src.database.instance_db import supabase
import bcrypt
import streamlit as st #type:ignore

def hass_password(password):
    return bcrypt.hashpw( password.encode(),bcrypt.gensalt()).decode()

def check_password(password,hased_password):
    return bcrypt.checkpw(password.encode(),hased_password.encode())

def check_teacher_username(username):
    responce=supabase.table('teachers').select("username").eq("username",username).execute()
    return len(responce.data)>0

def teacher_register(username,password,name):
    data={
        'username':username,
        'password':hass_password(password),
        'name':name
    }
    response=supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username,password):
    response=supabase.table('teachers').select('*').eq('username',username).execute()
    if response.data:
        teacher=response.data[0]
        if check_password(password,teacher['password']):
            return teacher
    return None

def get_all_students():
    responce=supabase.table("students").select("*").execute()
    return responce.data

def create_student(new_name,face_embedding=None,voice_embedding=None):
    data={
        'name':new_name,
        'face_embedding':face_embedding,
        'voice_embedding':voice_embedding
    }
    response=supabase.table("students").insert(data).execute()
    return response.data
     
         
def create_subject(sub_code,sub_name,section,teacher_id):
    data={
          "subject_code":sub_code,
            "name":sub_name,
            "section":section,
            "teacher_id":teacher_id
    }
    response=supabase.table("subjects").insert(data).execute()
    return response.data

def enroll_student_to_subject(student_id,subject_id):
    data={'student_id':student_id,
          'subject_id':subject_id}
    responce=supabase.table('subject_students').insert(data).execute()
    return responce.data
    
def unenroll_student_to_subject(student_id,subject_id):
    responce=supabase.table('subject_students').delete().eq('student_id',student_id).eq('subject_id',subject_id).eq('student_id',student_id).execute()
    return responce.data

@st.cache_data(ttl=30)
def get_student_subjects(student_id):
    responce=supabase.table('subject_students').select('*,subjects(*)').eq('student_id',student_id).execute()
    return responce.data


def get_student_attendance(student_id):
    responce=supabase.table('attendance_logs').select('*,subjects(*)').eq('student_id',student_id).execute()
    # st.write(responce.data)
    return responce.data


def create_attendance(logs):
    response=supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    responce=supabase.table('attendance_logs').select("*,subjects!inner(*)").eq('subjects.teacher_id',teacher_id).execute()
    return responce.data