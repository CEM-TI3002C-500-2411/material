import dash
from dash import html, dcc, callback, Input, Output, State
import plotly.express as px
import requests

backend_url = "http://localhost:8000"

def get_platforms():
    try:
        url = f"{backend_url}/platforms"
        response = requests.get(url)
        json_response = response.json()
        return json_response["platforms"]
    except Exception as e:
        return ["No se pudieron obtener las plataformas"]

def get_genres():
    try:
        url = f"{backend_url}/genres"
        response = requests.get(url)
        json_response = response.json()
        return json_response["genres"]
    except Exception as e:
        return ["No se pudieron obtener los géneros"]

def get_publishers():
    try:
        url = f"{backend_url}/publishers"
        response = requests.get(url)
        json_response = response.json()
        return json_response["publishers"]
    except Exception as e:
        return ["No se pudieron obtener los editores"]

def get_developers():
    try:
        url = f"{backend_url}/developers"
        response = requests.get(url)
        json_response = response.json()
        return json_response["developers"]
    except Exception as e:
        return ["No se pudieron obtener los desarrolladores"]
    
platforms = get_platforms()
genres = get_genres()
publishers = get_publishers()
developers = get_developers()

dash.register_page(__name__,
                   path="/predicciones",
                   title="Predicciones",
                   name="Predicciones")

layout = html.Div(children=[
    html.Div(children=[
        html.H3(children="Predicción de critic score"),
        html.Div(children=[
            html.Label(children="NA Sales", className="form-label"),
            dcc.Slider(
                min = 0,
                max = 100,
                step = 0.1,
                value = 50,
                marks = {0: "0", 25: "25", 50: "50", 75: "75", 100: "100"},
                tooltip = { "placement": "top", "always_visible": True },
                id = "NA_Sales"
            )
            ], className="mb-3"),
        html.Div(children=[
            html.Label(children="EU Sales", className="form-label"),
            dcc.Slider(
                min = 0,
                max = 100,
                step = 0.1,
                value = 50,
                marks = {0: "0", 25: "25", 50: "50", 75: "75", 100: "100"},
                tooltip = { "placement": "top", "always_visible": True },
                id = "EU_Sales"
            )
            ], className="mb-3"),
        html.Div(children=[
            html.Label(children="JP Sales", className="form-label"),
            dcc.Slider(
                min = 0,
                max = 100,
                step = 0.1,
                value = 50,
                marks = {0: "0", 25: "25", 50: "50", 75: "75", 100: "100"},
                tooltip = { "placement": "top", "always_visible": True },
                id = "JP_Sales"
            )
            ], className="mb-3"),
        html.Div(children=[
            html.Label(children="Other Sales", className="form-label"),
            dcc.Slider(
                min = 0,
                max = 100,
                step = 0.1,
                value = 50,
                marks = {0: "0", 25: "25", 50: "50", 75: "75", 100: "100"},
                tooltip = { "placement": "top", "always_visible": True },
                id = "Other_Sales"
            )
            ], className="mb-3"),
        dcc.Loading(children=[
            html.Div(children="", id="Critic_Score")
            ], type="circle"),
        html.Button(children="Obtener predicción", 
                    id="predicción critic score",
                    className="btn btn-lg btn-primary")
        ], className="p-5 text-center bg-body-tertiary rounded-3")
    ], className="container my-5")

@callback(
    Output("Critic_Score", "children"),
    Input("predicción critic score", "n_clicks"),
    [State("NA_Sales", "value"),
     State("EU_Sales", "value"),
     State("JP_Sales", "value"),
     State("Other_Sales", "value")]
)
def get_critic_score_prediction(n_clicks, NA_Sales, EU_Sales, JP_Sales, Other_Sales):
    try:
        if n_clicks:
            url = f"{backend_url}/predict_critic_score"
            data = {
                "NA_Sales": NA_Sales,
                "EU_Sales": EU_Sales,
                "JP_Sales": JP_Sales,
                "Other_Sales": Other_Sales
            }
            response = requests.post(url, json=data)
            response_json = response.json()
            prediction = response_json["prediction"]
            return f"El critic score será de: {prediction}"
    except Exception as e:
        return "No se pudo hacer la predicción"
        