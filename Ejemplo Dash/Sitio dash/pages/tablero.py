import dash
import pandas as pd
from dash import html, dash_table, dcc
import dash_ag_grid as dag
import plotly.express as px

df = pd.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

fig1 = px.scatter(df, x="NA_Sales", y="EU_Sales", size="Global_Sales", color="Developer")

dash.register_page(__name__,
                   path="/tablero",
                   title="Tablero de datos",
                   name="Tablero de datos")

layout = html.Div(children=[
    html.Div(children=[
        html.Div(children=[
            html.H1(children="Ventas anuales", className="text-body-emphasis"),
            dash_table.DataTable(data=df.to_dict("records"), page_size=10)
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
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
            html.Img(src="/assets/images/chart.jpg",
                     alt="Ventas por consola",
                     className="img-fluid"),
            html.P(children="Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum, quisquam.",
                   className="col-lg-8 mx-auto fs-5 text-muted")
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
    html.Div(children=[
        html.Div(children=[
            html.H1(children="Proyección de ventas", className="text-body-emphasis"),
            html.Img(src="/assets/images/chart.jpg",
                     alt="Proyección de ventas",
                     className="img-fluid"),
            html.P(children="Lorem ipsum dolor sit amet consectetur adipisicing elit. Rerum, quisquam.",
                   className="col-lg-8 mx-auto fs-5 text-muted")
            ], className="p-5 text-center bg-body-tertiary rounded-3")
        ], className="container my-5"),
    ])