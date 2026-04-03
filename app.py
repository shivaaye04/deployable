from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def root():
    return {"message": "API is working"}

@app.post("/predict")
def predict(features: list):
    df = pd.DataFrame([features])
    pred = model.predict(df)
    return {"prediction": pred.tolist()}