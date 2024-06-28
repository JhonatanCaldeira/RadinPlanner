import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os

st.title("Radin Planner")

backend_url = os.getenv("BACKEND_URL", "http://backend:8000")

user_id = st.session_state.get("user_id", None)

def get_expenses(user_id):
    response = requests.get(f"{backend_url}/users/{user_id}/expenses/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching expenses: {response.status_code}")
        return []
def add_expense(user_id, amount, category, description, date):
    expense_data = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date.isoformat(),  # Convertir l'objet datetime en chaîne de caractères ISO 8601
        "user_id": user_id
    }
    response = requests.post(f"{backend_url}/expenses/", json=expense_data)
    # st.write(expense_data)
    if response.status_code == 201:
        return response.json()
    else:
        # st.error(f"Error adding expense: {response.status_code}\n{response.text}")
        return None
    
def login_user(username, password):
    st.write(username, password)

    response = requests.get(f"{backend_url}/login/{username}/{password}/")#, json=login_data)
    if response.status_code == 200:
        return response.json()  # Assuming the backend returns user data on successful login
    else:
        st.error(f"Login failed: {response.status_code}\n{response.text}")
        return None
    
def register_user(username, password):
    nb_bdd = requests.post(f"{backend_url}/login/")
    register_data = {
        "id"      : 5 ,
        "username": username,
        "password": password
    }
    response = requests.post(f"{backend_url}/register/", json=register_data)
    if response.status_code == 201:
        return response.json()  # Assuming the backend returns user data on successful registration
    else:
        st.error(f"Registration failed: {response.status_code}\n{response.text}")
        return None


if user_id == None:
    # Sélecteur de page
    page = st.radio("Select a page", ("Login", "Register"))

    # Page d'authentification
    if page == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user_id = login_user(username, password)
            st.session_state.user_id = user_id

            if user_id:
                st.success(f"Logged in as {username}")
            # Logic for user login can be added here

    # Page d'inscription
    elif page == "Register":
        st.title("Register")
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Choose a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Register"):
            if new_password == confirm_password:
                register_user(new_username, new_password)
                st.success("User registered successfully")

else:
    # st.sidebar.title("User Information")
    # user_id = st.sidebar.number_input("User ID", min_value=1)

    st.sidebar.title("Add Expense")
    amount = st.sidebar.number_input("Amount", min_value=0.0, step=0.01)
    category = st.sidebar.text_input("Category")
    description = st.sidebar.text_area("Description")
    date = st.sidebar.date_input("Date", value=datetime.now().date())

    if st.sidebar.button("Add Expense"):
        add_expense(user_id, amount, category, description, date)
        st.sidebar.success("Expense added!")

    expenses = get_expenses(user_id)
    df = pd.DataFrame(expenses)

    st.dataframe(df)

    if not df.empty:
        st.bar_chart(df.groupby('category')['amount'].sum())
        st.line_chart(df.groupby('date')['amount'].sum())
