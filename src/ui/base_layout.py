import streamlit as st #type:ignore
def style_backgroud_home():
    st.markdown("""
        <style>    
            .stApp {
                background: #393D3F !important
            }
           [data-testid="stColumn"] > div {
            background-color: #EBEEFD !important;
            padding: 2.5rem !important;
            border-radius: 2rem !important;
        }
        </style>
    """,unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&family=Outfit:wght@100..900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

    # Hide Header 
    MainMenu {display:none;}
    footer {display:none;}
    [data-testid="stHeader"] 
    {display:none;}

    .block-container
        {
            padding-top:1.5 rem !important;
        }

    h1 {
        font-family: 'Oswald', sans-serif !important;
        font-weight: 700 !important; 
        font-size: 3.5rem !important;
        line-height:1.1 limportant;
        margin-bottom:Ørem !important;
        }
    h2 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 1.5rem !important;
        line-height:1.1 !important;
        text-align:center;
        color:#f0b618 !important;
        margin-bottom:Ørem !important;
        }

    h3, h4, p, span {
            font-family: 'Outfit', sans-serif;
        }
    /* Primary Button */
    button[kind="primary"] {
        background-color: #EB459E !important;
        color: white !important;
        border-radius: 1.5rem !important;
        border: none !important;
    }

    /* Secondary Button */
    button[kind="secondary"] {
        background-color: #5865F2 !important;
        color: white !important;
        border-radius: 1.5rem !important;
        border: none !important;
    }

    /* Tertiary Button */
    button[kind="tertiary"] {
        background-color: #e9c46a !important;
        color: black !important;
        border-radius: 1.5rem !important;
        border: none !important;
    }
        div.stButton > button {
        transition: all 0.2s ease !important;
    }

    div.stButton > button:hover {
        transform: scale(1.1) !important;
        cursor: pointer !important;
    }
    </style>
    """, unsafe_allow_html=True)


