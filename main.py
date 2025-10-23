from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data 

@app.get("/")
def hello():
    return {'Message':'welcome to inturnx'}

@app.get('/about')
def about():
    return {'message':'A platform for genuine internship'}

