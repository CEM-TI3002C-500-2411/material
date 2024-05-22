import dash
from dash import Dash, html, dcc, Output, Input, State, ALL

external_stylesheets = [
    {"href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
     "rel": "stylesheet",
     "integrity": "sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH",
     "crossorigin": "anonymous"},
    {"rel": "stylesheet",
     "href": "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"}
]

external_scripts = [
    {"src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
     "integrity": "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz",
     "crossorigin": "anonymous"}
]    

app = Dash(__name__, 
           external_stylesheets=external_stylesheets, 
           external_scripts=external_scripts,
           use_pages=True)

header = html.Div(children = [
    html.Header(children = [
        dcc.Link(children = [
            html.Span(children = [
                html.I(className="bi bi-controller me-2"),
                "Ventas de videojuegos"
                ],className="fs-2 main-title")
            ], href="/", 
               className="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none"),
        html.Ul(children=[
            html.Li(children = [
                dcc.Link(children="Inicio",
                       href="/",
                       className="nav-link active", id={"type": "page-link", "page": "/"})
                ], className="nav-item"),
            html.Li(children = [
                dcc.Link(children="Tablero",
                       href="/tablero",
                       className="nav-link", id={"type": "page-link", "page": "/tablero"})
                ], className="nav-item"),
            html.Li(children = [
                dcc.Link(children="Hallazgos",
                       href="/hallazgos",
                       className="nav-link", id={"type": "page-link", "page": "/hallazgos"})
                ], className="nav-item"),
            html.Li(children = [
                dcc.Link(children="Predicciones",
                       href="/predicciones",
                       className="nav-link", id={"type": "page-link", "page": "/predicciones"})
                ], className="nav-item"),
            ], className="nav nav-pills")
        ], className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom")
    ], className="container")

footer = html.Div(children=[
    html.Footer(children=[
        html.P(children="© 2024 Company, Inc",
               className="col-md-4 mb-0 text-body-secondary"),
        html.Ul(children=[
            html.Li(children=[
                dcc.Link(children="Inicio",
                       href="/",
                       className="nav-link px-2 text-body-secondary")
                ], className="nav-item"),
            html.Li(children=[
                dcc.Link(children="Tablero",
                       href="/tablero",
                       className="nav-link px-2 text-body-secondary")
                ], className="nav-item"),
            html.Li(children=[
                dcc.Link(children="Hallazgos",
                       href="/hallazgos",
                       className="nav-link px-2 text-body-secondary")
                ], className="nav-item"),
            html.Li(children=[
                dcc.Link(children="Predicciones",
                       href="/predicciones",
                       className="nav-link px-2 text-body-secondary")
                ], className="nav-item"),
            ], className="nav col-md-4 justify-content-end")
        ], className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top")
], className="container")

app.layout = html.Div(children = [
    dcc.Location(id="url"),
    header, 
    dash.page_container, 
    footer])

@app.callback(
    Output({"type": "page-link", "page": ALL}, "className"),
    Input("url", "pathname"),
    State({"type": "page-link", "page": ALL}, "id")
)
def update_active_link(pathname, id):
    return ["nav-link active" if x["page"] == pathname else "nav-link" for x in id]

if __name__ == "__main__":
    app.run(debug=True)