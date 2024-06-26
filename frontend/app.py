import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.title("Expense Tracker")

backend_url = "http://backend:8000"

def get_expenses(user_id):
    response = requests.get(f"{backend_url}/users/{user_id}/expenses/")
    return response.json()

def add_expense(user_id, amount, category, description, date):
    expense_data = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
        "user_id": user_id
    }
    response = requests.post(f"{backend_url}/expenses/", json=expense_data)
    return response.json()

st.sidebar.title("Add Expense")
user_id = st.sidebar.number_input("User ID", min_value=1)
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
