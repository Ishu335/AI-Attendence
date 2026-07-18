import streamlit as st # type:ignore
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
    <div style="
        background: white;
        border-left: 8px solid #EB459E;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid black;
        margin-bottom: 20px;">
        <h3 style="margin:0; color:#1e293b; font-size:1.5rem;">{name}</h3>
        <p style="color:#64748b; margin:10px 0;">
            Code:
            <span style="
                background:#E0E3FF;
                color:#5865F2;
                padding:2px 8px;
                border-radius:5px;">
                {code}
            </span>
        </p>
        <p style="color:#64748b; margin:5px 0;">
            Section: <b>{section}</b>
        </p>
    """

    if stats:
        from textwrap import dedent
        html += dedent("""
        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:10px;">
        """)

        for icon, label, value in stats:
            html += dedent(f"""
            <div style="
                background:#24292E;
                padding:6px 12px;
                border-radius:12px;
                text-color:black;
                font-size:0.9rem;
            ">
                {icon} <b>{value}</b> {label}
            </div>
            """)

        html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()