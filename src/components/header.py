import streamlit as st #type:ignore
import base64


def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


def header_home():

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
        gap:20px;
        width:100%;
        margin-bottom:20px; /* Increase bottom space */
    }

    .logo-img img{
    width:100px;
    height:100px;
    display:block;
    border-radius:20%;
    object-fit:cover;
    border:3px solid #FDB604;
}

    .title-container{
        display:flex;
        flex-direction:column;
        justify-content:center;
    }

   .main-title{
    margin:0;
    padding:0;
    line-height:1;
    font-size:2rem;
    font-weight:800;   /* not 850px */

    white-space:nowrap;    /* Keep text on one line */
    overflow:hidden;

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
}

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    }

    .sub-title{
        color:#C7D2FE;
        margin:0 !important;
        padding:0 !important;
        line-height:1.2;
        font-size:1.1rem;
        letter-spacing:1px;
        text-align:left;
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
            <p class="sub-title">
                Smart Attendance Management System
            </p>
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
        gap:20px;
        width:100%;
        margin-bottom:20px; /* Increase bottom space */
    }

    .logo-img img{
    width:70px;
    height:70px;
    display:block;
    border-radius:20%;
    object-fit:cover;
    border:2px solid #FEBB2F;
}

    .title-container{
        display:flex;
        flex-direction:column;
        justify-content:center;
    }

    .main-title{
    margin:0 !important;
    padding:0 !important;
    line-height:1.1;

    font-size:3rem;
    font-weight:700;

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
}

    .sub-title{
        color:#C7D2FE;
        margin:0 !important;
        padding:0 !important;
        line-height:0.5;
        font-size:0.6 rem;
        letter-spacing:1px;
        text-align:left;
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
            <p class="sub-title">
                Smart Attendance Management System
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

