from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Dummy user data for demonstration purposes
fake_users = {
    "user1": {"password": "password1", "name": "John Doe"},
    "user2": {"password": "password2", "name": "Jane Doe"},
}

class User(BaseModel):
    username: str
    password: str

class Record(BaseModel):
    id: int
    data: str

def authenticate_user(user: User):
    if user.username in fake_users and fake_users[user.username]["password"] == user.password:
        return user.username
    raise HTTPException(status_code=401, detail="Invalid credentials")

def get_user_records(username: str):
    # In a real application, this is where you would retrieve the records from a database
    # For demonstration purposes, we'll return dummy data
    return {1: "Record 1 data", 2: "Record 2 data"}

@app.post("/login")
def login_for_access_token(user: User):
    username = authenticate_user(user)
    return {"access_token": username}

@app.get("/records/{record_id}")
def get_record_by_id(record_id: int, current_user: str = Depends(authenticate_user)):
    records = get_user_records(current_user)
    if record_id not in records:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"record_id": record_id, "data": records[record_id]}



#parse data from an .ini file and then format it into a specific output format

import configparser

# Assuming the data is in a file named data.ini
config = configparser.ConfigParser()
config.read('data.ini')

output_list = []

for section in config.sections():
    a = config.get(section, 'a')
    b = config.get(section, 'b')
    
    # Convert 'a' to the desired format
    a = a.lower() if 'dbname' in a else 'dbName'

    output_list.append({"a": a, "b": b})

print(output_list)
