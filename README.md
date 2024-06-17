# T2SQL-ChatBot

## Project Documentation

This documentation provides a comprehensive guide to setting up and using the project, which allows users to connect to a MySQL database and run natural language queries that are converted into SQL queries using the LangChain library and Google's PaLM model. The application is built using Streamlit, a powerful framework for creating web applications in Python.

### Overview

The project consists of three main components:

1. **Setup Database Connection**: Allows users to input their database credentials and establish a connection to the MySQL database.
2. **Run Natural Language Queries**: Provides an interface for users to enter queries in natural language, which are then converted to SQL queries and executed against the database.
3. **Main Application**: Manages navigation between the setup and query pages and initializes the application state.

### Project Structure

The project contains the following files:

- `connection.py`: Contains the functionality for setting up the database connection.
- `query.py`: Contains the functionality for running natural language queries.
- `main.py`: The main script that combines the setup and query functionalities and handles page navigation.
- `requirements.txt`: Lists the Python packages required to run the project.

### Getting Started

#### Prerequisites

Ensure you have the following installed:

- Python 3.11
- MySQL database


Make sure that you have the following details for testing the Chatbot:

- Google PaLM API key
- Database Details: Username, Password, Hostname and Database Name
