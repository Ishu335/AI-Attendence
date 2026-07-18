import streamlit as st #type:ignore

def teacher_reg_style():

    st.markdown("""
    <style>
    /* ===== BACKGROUND ===== */

    [data-testid="stAppViewContainer"]{
        background:#262730 !important;
    }

    /* ===== CONTAINER ===== */

    .block-container{
        max-width:850px !important;
        padding-top:0rem !important;
        padding-bottom:0rem !important;
    }

    /* ===== FLOATING GLOW EFFECTS ===== */

    [data-testid="stAppViewContainer"]::before{
        content:"";
        position:fixed;
        width:280px;
        height:280px;
        top:-200px;
        left:-100px;
        border-radius:50%;
        background:rgba(255,255,255,0.40);
        filter:blur(120px);
        z-index:-1;
    }

    [data-testid="stAppViewContainer"]::after{
        content:"";
        position:fixed;
        width:300px;
        height:300px;
        bottom:-100px;
        right:-100px;
        border-radius:50%;
        background:rgba(148,163,184,0.35);
        filter:blur(120px);
        z-index:-1;
    }

    /* ===== TITLE ===== */

    .main-heading{
        text-align:center;
        font-size:2.3rem;
        font-weight:700;
        color:black !important;
        margin-top:0px;
        margin-bottom:20px;
    }

    /* ===== FORM CARD ===== */

    .form-card{
        background:rgba(255,255,255,0.80);
        backdrop-filter:blur(15px);
        border-radius:24px;
        padding:25px;
        box-shadow:0 10px 30px rgba(0,0,0,0.08);
    }

    /* ===== LABELS ===== */

    label{
        color:black !important;
        font-weight:500;
    }

    /* ===== INPUTS ===== */

    .stTextInput input{
        background:white !important;
        color:black !important;
        border-radius:14px !important;
        border:1px solid #CBD5E1 !important;
        height:48px;
    }
    .stTextInput label 
    {
        color: white !important; 
        font-size: 18px !important;
        font-weight: 600 !important;
    }

    .stTextInput input::placeholder{
        color:#64748B !important;
    }

    /* ===== BUTTONS ===== */

    div.stButton > button{
        border-radius:14px !important;
        height:50px !important;
        font-weight:600 !important;
        transition:all 0.3s ease !important;
    }

    div.stButton > button:hover{
        transform:translateY(-2px);
    }

    /* ===== FOOTER ===== */

    .footer-text{
        text-align:center;
        color:orange !important;
        margin-top:15px;
        font-size:14px;
    }

    /* ===== REMOVE STREAMLIT SPACING ===== */

    [data-testid="stToolbar"]{
        display:none;
    }

    footer{
        display:none;
    }

    </style>
    """, unsafe_allow_html=True)