import streamlit as st
import time
import requests
st.set_page_config(
    page_title="Precedent Summariser",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'http://fakeurl.com',
        'Report a bug': "http://fakeurl.com",
        'About': "# Experimental"
    }
)

case = st.text_area("Case", "")
reference = st.text_area("References", "")


def load_response_from_api():
    with st.spinner('Loading...'):
        response = requests.get("http://localhost:8888/health").json()
        if response.get('status') != 'ok':
            return 'error'
    return response


if st.button('Analyse'):
    response = load_response_from_api()
    st.write(response)
