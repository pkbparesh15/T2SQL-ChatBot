# setup_connection.py

import streamlit as st
from langchain import SQLDatabase
from langchain.llms import GooglePalm
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import create_engine

def setup_database_connection(api_key):
    st.title("Setup Database Connection")

    # Database Connection Details
    st.header("Database Connection")
    db_user = st.text_input("Database User", "root")
    db_password = st.text_input("Database Password", "root", type="password")
    db_host = st.text_input("Database Host", "localhost")
    db_name = st.text_input("Database Name", "sakila")
    
    

    if st.button("Connect to Database"):
        try:
            connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
            engine = create_engine(connection_string)
            st.session_state.connection = engine.connect()
            st.success("Connected to Database")

            # Wrap the connection with SQLDatabase
            db = SQLDatabase(engine)

            # Initialize the LLM and database chain if connection is established
            llm = GooglePalm(google_api_key=api_key, temperature=0)
            st.session_state.db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
            st.success("Initialized db_chain successfully")

            # Modify prompt to explicitly ask for the SQL query and result
            '''
            prompt_template = """
                        You are a helpful assistant that converts natural language queries into SQL and retrieves the result.
                        Please return final result, and return the syntax of SQL query not the exact query.

                        Natural language query: {query}

                        SQL query:
                        Result:
                        """

            st.session_state.db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True,
                                                                  prompt_template=prompt_template)
            st.success("Initialized db_chain successfully")
            '''

        except Exception as e:
            st.error(f"Error connecting to database: {e}")