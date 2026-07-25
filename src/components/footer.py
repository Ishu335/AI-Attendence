import streamlit as st  # type:ignore


def footer_home():
    st.markdown("""
    <style>

    .footer-container{
        width:100%;
        height:120px;
        margin-top:30px;
        padding:12px 20px;
        border-radius:16px;

        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        gap:8px;

        border:1px solid rgba(255,255,255,0.15);
        background:rgba(255,255,255,0.04);
        backdrop-filter:blur(12px);
        box-sizing:border-box;
        overflow:hidden;
    }

    .footer-title{
        margin:0;
        font-size:1.25rem;
        font-weight:700;
        line-height:1;
    }

    .footer-title span{
        background:linear-gradient(
            90deg,
            #60A5FA,
            #22D3EE,
            #A78BFA
        );
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .footer-subtitle{
        margin:0;
        font-size:0.82rem;
        color:#CBD5E1;
        text-align:center;
        line-height:1.2;
    }

    .feature-row{
        display:flex;
        justify-content:center;
        align-items:center;
        flex-wrap:wrap;
        gap:6px;
    }

    .feature-badge{
        padding:3px 10px;
        border-radius:999px;
        font-size:0.68rem;
        color:#E2E8F0;
        background:#5865F2;
        border:1px solid rgba(255,255,255,.08);
        line-height:1.2;
    }

    .footer-copy{
        margin:0;
        font-size:0.70rem;
        color:#94A3B8;
        text-align:center;
        line-height:1.2;
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
            <button class="feature-badge">🎭 Face AI</button>
            <button class="feature-badge">🎙️ Voice AI</button>
            <button class="feature-badge">⚡ Real-Time</button>
            <button class="feature-badge">☁️ Cloud</button>
            <button class="feature-badge">🤖 AI</button>
        </div>
        <div class="footer-copy">
            © 2026 <b>VisionVoice AI</b> • Built with ❤️ using Python & Streamlit
        </div>
    </div>
    """, unsafe_allow_html=True)