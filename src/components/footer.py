import streamlit as st #type:ignore

def  footer_home():
    st.markdown("""
    <style>
    .footer-container{
        margin-top:30px;
        height:150px;
        border-radius:16px;
        padding:12px 20px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        gap:10px;
        border:1px solid white;
        backdrop-filter:blur(12px);
        overflow:hidden;
    }
    .footer-title{
        font-size:1.35rem;
        font-weight:700;
        line-height:1;
    }
    .footer-title span{
        background:linear-gradient(90deg,#60A5FA,#22D3EE,#A78BFA);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }
    .footer-subtitle{
        font-size:.88rem;
        color:#CBD5E1;
        margin:0;
    }
    .feature-row{
        display:flex;
        justify-content:center;
        flex-wrap:wrap;
        gap:8px;
    }

    .feature-badge{
        padding:4px 10px;
        border-radius:999px;
        font-size:.72rem;
        color:#E2E8F0;
        background:rgba(255,255,255,.08);
        border:1px solid rgba(255,255,255,.06);
        line-height:1.2;
    }

    .footer-copy{
        font-size:.75rem;
        color:#94A3B8;
        text-align:center;
    }

    </style>

    <div class="footer-container">
        <div class="footer-title">
            <span>VisionVoice AI</span>
        </div>
        <div class="footer-subtitle">
            AI Powered Face & Voice Attendance
        </div>
        <div class="feature-row">
            <div class="feature-badge">🎭 Face AI</div>
            <div class="feature-badge">🎙 Voice AI</div>
            <div class="feature-badge">⚡ Real-Time</div>
            <div class="feature-badge">☁ Cloud</div>
            <div class="feature-badge">🤖 AI</div>
        </div>
        <div class="footer-copy">
            © 2026 <b>AttendAI</b> • Built with ❤️ using Python & Streamlit
        </div>
    </div>
    """, unsafe_allow_html=True)