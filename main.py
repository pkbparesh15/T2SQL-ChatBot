# main.py

import streamlit as st
from streamlit_option_menu import option_menu
from connection import setup_database_connection
from query import run_queries

api_key = "AIzaSyDn6Q_q3-3mdDXL_1bLOU24Vfe3rCrjtg8"

# Initialize session state
if 'connection' not in st.session_state:
    st.session_state.connection = None
if 'db_chain' not in st.session_state:
    st.session_state.db_chain = None

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Setup Connection", "Run Queries"],
        icons=["plug", "play"],
        menu_icon="cast",
        default_index=0,
    )

# Page routing
if selected == "Setup Connection":
    setup_database_connection(api_key)
elif selected == "Run Queries":
    run_queries()
