# run_queries.py

import streamlit as st


def run_queries():
    st.title("Run Natural Language Queries")

    if st.session_state.connection:
        query = st.text_area("Enter your query in natural language:")
        if st.button("Run Query"):
            if st.session_state.db_chain:
                try:
                    # Use the db_chain to process the natural language query and generate the SQL query
                    result = st.session_state.db_chain(query)
                    st.write(result['result'])

                except Exception as e:
                    st.error(f"Error running query: {e}")
            else:
                st.error("db_chain is not initialized. Please setup the connection again.")
    else:
        st.warning("Please setup the database connection first on the Setup Connection page.")
