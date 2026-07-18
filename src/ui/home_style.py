import streamlit as st #type:ignore
def home_style_page():
    
    st.markdown("""
    <style>
    /* Animated Background */
.stApp{
    background:linear-gradient(
        135deg,
        #0F172A,
        #1E293B,
        #312E81,
        #0F172A
    );
    background-size:400% 400%;
    animation:bgMove 15s ease infinite;
}

@keyframes bgMove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Glowing Orb 1 */
[data-testid="stAppViewContainer"]::before{
    content:"";
    position:fixed;
    width:350px;
    height:350px;
    background:rgba(99,102,241,0.30);
    border-radius:50%;
    filter:blur(130px);
    top:10%;
    left:5%;
    animation:float1 10s ease-in-out infinite;
    z-index:-2;
}

/* Glowing Orb 2 */
[data-testid="stAppViewContainer"]::after{
    content:"";
    position:fixed;
    width:300px;
    height:300px;
    background:rgba(59,130,246,0.25);
    border-radius:50%;
    filter:blur(130px);
    bottom:10%;
    right:5%;
    animation:float2 12s ease-in-out infinite;
    z-index:-2;
}

/* Extra Glow */
.main::before{
    content:"";
    position:fixed;
    width:250px;
    height:250px;
    background:rgba(236,72,153,0.25);
    border-radius:50%;
    filter:blur(100px);
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    z-index:-2;
}

/* Grid Pattern */
[data-testid="stAppViewContainer"]{
    background-image:
    linear-gradient(
        rgba(255,255,255,0.03) 1px,
        transparent 1px
    ),
    linear-gradient(
        90deg,
        rgba(255,255,255,0.03) 1px,
        transparent 1px
    );
    background-size:40px 40px;
}

/* Floating Animation */
@keyframes float1{
    0%,100%{
        transform:translateY(0px);
    }
    50%{
        transform:translateY(-50px);
    }
}

@keyframes float2{
    0%,100%{
        transform:translateY(0px);
    }
    50%{
        transform:translateY(50px);
    }
}

    </style>
    """, unsafe_allow_html=True)
