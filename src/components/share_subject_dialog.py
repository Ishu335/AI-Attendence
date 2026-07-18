import streamlit as st #type:ignore
import segno 
import io

@st.dialog('Share Subject')
def share_subject_dialog(subject_name,subject_code):
    app_domain=st.secrets['DOMAIN_URL']
    join_url=f"{app_domain}?join-code={subject_code}"

    st.markdown("### Scan to Join")



    qr=segno.make(join_url)
    out=io.BytesIO()
    qr.save(out,kind='png',scale=10,border=1)

    col1,col2=st.columns(2)
    with col1:
        st.markdown("#### Code Link")
        st.code(join_url, language='text')
        st.code(subject_code,language='text')
        st.info('Copy this link to share on Whatsapp or Email')
    with col2:
        st.markdown("#### Scan to Join")
        st.image(out.getvalue(),width="stretch",caption='QR Code to Join a Class')