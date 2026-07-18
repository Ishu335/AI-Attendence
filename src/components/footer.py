import streamlit as st #type:ignore

def footer_home():

    st.markdown("""
    <style>

    .footer-container{
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        padding:20px 0;
        border-top:1px solid rgba(255,255,255,0.1);
    }

    .footer-subtitle{
        color:#C7D2FE;
        font-size:0.95rem;
        letter-spacing:1px;
        text-align:center;
        margin-bottom:8px;
    }

    .footer-copy{
        color:#94A3B8;
        font-size:0.85rem;
        text-align:center;
    }

    </style>

    <div class="footer-container">
        <div class="footer-subtitle">
            Smart Attendance Management System
        </div>
        <div class="footer-copy">
            © 2026 Attendance System | Powered by AI & Face Recognition
        </div>
    </div>
    """, unsafe_allow_html=True)