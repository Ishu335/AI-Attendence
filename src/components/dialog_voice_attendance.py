import streamlit as st# type:ignore
from src.pipline.voice_pipeline import process_bulk_audio
@st.dialog("Voice Attendance")
def voice_attendance_dialog(Selected_subject_id):
    st.write("Record Audio of Student Saying I am Present. AI will recognize the Student Voice ")

    audio_data=None
    audio_data=st.audio_input("Reacord Classroom Audio")

    if st.button('Analyze Audio',width='stretch',type='primary'):
        with st.spinner('Processing Audio Data...'):
            process_bulk_audio(audio_data)