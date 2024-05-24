import dash
import pandas as pd
from dash import html, dash_table, dcc
import dash_ag_grid as dag
import plotly.express as px
import requests

backend_url = "http://localhost:8000"

def get_table():
    try:
        url = f"{backend_url}/sample"
        response = requests.get(url)
        json_response = response.json()
        return pd.DataFrame(json_response)
    except Exception as e:
        return pd.DataFrame()

def get_sales_chart():
    try:
        url = f"{backend_url}/sales_chart_data"
        response = requests.get(url)
        json_response = response.json()
        df = pd.DataFrame(json_response)
        return px.scatter(df, x="NA_Sales", y="EU_Sales", size="Global_Sales", color="Developer")
    except Exception as e:
        return None
    
def get_sales_by_platform():
    try:
        url = f"{backend_url}/sales_by_platform"
        response = requests.get(url)
        json_response = response.json()
        df = pd.DataFrame(json_response)
        return px.bar(df, x="Platform", y="Global_Sales", color="Platform")
    except Exception as e:
        return None
    
def get_critic_score_by_year():
    try:
        url = f"{backend_url}/critic_score_mean_by_year"
        response = requests.get(url)
        json_response = response.json()
        df = pd.DataFrame(json_response)
        return px.line(df, x="Year_of_Release", y="Critic_Score", color="Platform")
    except Exception as e:
        return None

df = get_table()
fig1 = get_sales_chart()
fig2 = get_sales_by_platform()
fig3 = get_critic_score_by_year()

dash.register_page(__name__,
                   path="/tablero",
                   title="Tablero de datos",
                   name="Tablero de datos")

layout = html.Div(children=[
    # html.Div(children=[
    #     html.Div(children=[
    #         html.H1(children="Ventas anuales", className="text-body-emphasis"),
    #         dash_table.DataTable(data=df.to_dict("records"), page_size=10)
    #         ], className="p-5 text-center bg-body-tertiary rounded-3")
    #     ], className="container my-5"),
    html.Div(children=[
        html.Iframe(src="https://public.tableau.com/views/ejemplovisualparaelreto/Dashboardreto?:showVizHome=no&:embed=true",
                    width="100%",
                    height="800px"),
    ], className="container"),
    html.Div(children=[
        html.Div(children=[
            html.H1(children="Ventas anuales", className="text-body-emphasis"),
            dag.AgGrid(rowData=df.to_dict("records"),
                       columnDefs = [{"field": x, 
                                      "filter": True,
                                      "sortable": True} for x in df.columns],
                       dashGridOptions={"pagination": True})
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
    html.Div(children=[
        html.Div(children=[
            html.H1(children="Ventas anuales", className="text-body-emphasis"),
            dcc.Graph(id="fig1", figure=fig1)
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
    html.Div(children=[
        html.Div(children=[
            html.H1(children="Ventas por consola", className="text-body-emphasis"),
            dcc.Graph(id="fig2", figure=fig2)
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
    html.Div(children=[
        html.Div(children=[
            html.H1(children="Critic score promedio por año", className="text-body-emphasis"),
            dcc.Graph(id="fig3", figure=fig3)
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
    ])