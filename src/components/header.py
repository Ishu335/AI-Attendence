import streamlit as st  # type:ignore
import base64


def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def header_home():

    logo = get_base64("img/logo.png")

    st.markdown("""
    <style>

    /* Reduce Streamlit top padding */
    .block-container{
        padding-top:0rem !important;
    }

    .header-wrapper{
        display:flex;
        justify-content:center;
        align-items:center;
        gap:20px;
        width:100%;

        margin-top:-15px;      /* Move header upward */
        margin-bottom:60px;    /* Increase bottom spacing */
    }

    .logo-img img{
        width:100px;
        height:100px;
        display:block;
        object-fit:cover;
        border-radius:20%;
    }

    .title-container{
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:flex-start;
        gap:0;
    }

    .main-title{
        margin:0;
        padding:0;
        line-height:1;
        font-size:2.6rem;
        font-weight:800;
        white-space:nowrap;

        background:linear-gradient(
            90deg,
            #60A5FA,
            #22D3EE,
            #A78BFA
        );

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        background-clip:text;

        display:inline-block;
        margin-bottom:-6px;
    }

    .sub-title{
        margin:0;
        padding:0;
        color:#C7D2FE;
        font-size:1rem;
        font-weight:500;
        line-height:1;
        letter-spacing:.6px;
        margin-top:-2px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="header-wrapper">
        <div class="logo-img">
            <img src="data:image/png;base64,{logo}">
        </div>
        <div class="title-container">
            <h1 class="main-title">VisionVoice</h1>
            <p class="sub-title">Smart Attendance Management System</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def header_dashboard():

    logo = get_base64("img/logo.png")

    st.markdown("""
    <style>

    .block-container{
        padding-top:0rem !important;
    }

    .header-wrapper{
        display:flex;
        justify-content:center;
        align-items:center;
        gap:16px;
        width:100%;

        margin-top:-10px;      /* Reduce top gap */
        margin-bottom:40px;    /* Increase bottom gap */
    }

    .logo-img img{
        width:70px;
        height:70px;
        display:block;
        object-fit:cover;
        border-radius:20%;
    }

    .title-container{
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:flex-start;
        gap:0;
    }

    .main-title{
        margin:0;
        padding:0;
        line-height:1;
        font-size:3rem;
        font-weight:800;

        background:linear-gradient(
            90deg,
            #60A5FA,
            #22D3EE,
            #A78BFA
        );

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        background-clip:text;

        display:inline-block;
        margin-bottom:-8px;
    }

    .sub-title{
        margin:0;
        padding:0;
        color:#C7D2FE;
        font-size:.75rem;
        font-weight:500;
        line-height:1;
        letter-spacing:.6px;
        margin-top:-2px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="header-wrapper">
        <div class="logo-img">
            <img src="data:image/png;base64,{logo}">
        </div>
        <div class="title-container">
            <h1 class="main-title">VisionVoice</h1>
            <p class="sub-title">Smart Attendance Management System</p>
        </div>
    </div>
    """, unsafe_allow_html=True)