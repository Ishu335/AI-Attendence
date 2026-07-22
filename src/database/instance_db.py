from supabase import create_client, Client #type:ignore
import streamlit as st #type:ignore

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)