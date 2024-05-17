from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

class CriticScoreModel(BaseModel):
    NA_Sales: float
    EU_Sales: float
    JP_Sales: float
    Other_Sales: float

class RatingModel(BaseModel):
    Platform: str
    Genre: str
    Publisher: str
    Developer: str

df = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
df = df.dropna(how="any")
gnb = joblib.load("modelo_gaussiano.joblib")
mnb = joblib.load("modelo_multinomial.joblib")

app = FastAPI()

@app.get("/sample")
async def sample():
    return df.head(10).to_dict(orient="records")

@app.get("/sales_chart_data")
async def sales_chart_data():
    return df[["NA_Sales", "EU_Sales", "Global_Sales", "Developer"]].to_dict(orient="records")

@app.get("/platforms")
async def platforms():
    return {"platforms": df["Platform"].unique().tolist()}

@app.get("/genres")
async def genres():
    return {"genres": df["Genre"].unique().tolist()}

@app.get("/publishers")
async def publishers():
    return {"publishers": df["Publisher"].unique().tolist()}

@app.get("/developers")
async def developers():
    return {"developers": df["Developer"].unique().tolist()}

@app.post("/predict_critic_score")
async def predict_critic_score(data: CriticScoreModel):
    pred_df = pd.DataFrame([data.model_dump()])
    prediction = gnb.predict(pred_df)[0]
    return {"prediction": prediction}

@app.post("/predict_rating")
async def predict_rating(data: RatingModel):
    pred_df = pd.DataFrame([data.model_dump()])
    pred_df = pd.get_dummies(pred_df)
    columns_df = pd.DataFrame(columns=mnb.feature_names_in_, dtype=bool)
    columns_df, pred_df = columns_df.align(pred_df, join="left", axis=1, fill_value=False)
    prediction = mnb.predict(pred_df)[0]
    return {"prediction": prediction}

@app.post("/predict_rating_probabilities")
async def predict_rating_probabilities(data: RatingModel):
    pred_df = pd.DataFrame([data.model_dump()])
    pred_df = pd.get_dummies(pred_df)
    columns_df = pd.DataFrame(columns=mnb.feature_names_in_, dtype=bool)
    columns_df, pred_df = columns_df.align(pred_df, join="left", axis=1, fill_value=False)
    # Función zip:
    # ["E", "M", "T"], [0.6, 0.1, 0.2] -> [("E", 0.6), ("M", 0.1), ("T", 0.2)]
    x = mnb.predict_log_proba(pred_df)[0]
    x = np.exp(x) / np.exp(x).sum()
    prediction = dict(zip(mnb.classes_, x))
    return prediction

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)