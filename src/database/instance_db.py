from supabase import create_client,client
import streamlit as st

supabase: client=create_client(
    st.secrets['SUPABASE_URL'],
    st.secrets['SUPABASE_KEY']
)