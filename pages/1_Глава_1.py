import streamlit as st

st.set_page_config(page_title="Глава 1 Здесь могла быть ваша реклама", page_icon="📖")

st.markdown(
    """
    <style>
    .chapter-title {
        font-family: 'Cinzel', serif;
        font-size: 42px;
        color: #a0522d;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px #000000;
    }
    .session-content {
        font-family: 'Georgia', serif;
        font-size: 18px;
        color: #f0e6d2;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background: linear-gradient(145deg, #2a2020, #3d3030);
        border-radius: 15px;
        box-shadow: 3px 3px 12px #1a1515;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

