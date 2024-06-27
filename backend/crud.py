import requests
from schemas import UserCreate, ExpenseCreate

SUPABASE_URL = "https://txnppunaxtmrfcqbmazl.supabase.co/rest/v1/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR4bnBwdW5heHRtcmZjcWJtYXpsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxOTM5NzM3NSwiZXhwIjoyMDM0OTczMzc1fQ.MdNhauall00lM4HNvTu5qmN03K6UcXMFoS70Y9Muk1w"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

def get_user(user_id: int):
    response = requests.get(f"{SUPABASE_URL}users?id=eq.{user_id}", headers=headers)
    response.raise_for_status()
    users = response.json()
    if users:
        return users[0]
    return None

def create_user(user: UserCreate):
    response = requests.post(f"{SUPABASE_URL}users", headers=headers, json=user.dict())
    response.raise_for_status()
    return response.json()

def create_expense(expense: ExpenseCreate):
    response = requests.post(f"{SUPABASE_URL}expenses", headers=headers, json=expense.dict())
    response.raise_for_status()
    return response.json()

def get_expenses(user_id: int, skip: int = 0, limit: int = 100):
    response = requests.get(f"{SUPABASE_URL}expenses?user_id=eq.{user_id}&limit={limit}&offset={skip}", headers=headers)
    response.raise_for_status()
    print(response.json())
    return response.json()