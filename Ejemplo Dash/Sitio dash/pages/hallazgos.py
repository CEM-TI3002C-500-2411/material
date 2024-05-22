import dash
from dash import html

dash.register_page(__name__,
                   path="/hallazgos",
                   title="Hallazgos",
                   name="Hallazgos")

layout = html.Div(children=[
        html.Div(children=[
            html.H2(children="Hallazgos relevantes", className="pb-2 border-bottom"),
            html.Div(children=[
                html.Div(children=[
                    html.Div(children=[
                        html.Div(children=[
                            html.H3(children="Género más jugado: Acción", className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold")
                            ], className="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1")
                        ], className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg hallazgo-1")
                    ], className="col"),
                html.Div(children=[
                    html.Div(children=[
                        html.Div(children=[
                            html.H3(children="Saga con más proyección de ventas: Mario", className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold")
                            ], className="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1")
                        ], className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg hallazgo-2")
                    ], className="col"),
                html.Div(children=[
                    html.Div(children=[
                        html.Div(children=[
                            html.H3(children="Plataforma con mayor proyección: PC", className="pt-5 mt-5 mb-4 display-6 lh-1 fw-bold")
                            ], className="d-flex flex-column h-100 p-5 pb-3 text-shadow-1")
                        ], className="card card-cover h-100 overflow-hidden text-bg-dark rounded-4 shadow-lg hallazgo-3")
                    ], className="col"),
                ], className="row row-cols-1 row-cols-lg-3 align-items-stretch g-4 py-5"),
            ], className="container px-4 py-5", id="custom-cards"),
        html.Div(children=[
            html.H2(children="Más datos relevantes", className="pb-2 border-bottom"),
            html.Div(children=[
                html.Div(children=[
                    html.H3(children=[
                        html.I(className="bi bi-currency-dollar me-2"),
                        html.Span(children="Ventas"),
                        ], className="fs-2 text-body-emphasis"),
                    html.P(children="Lorem ipsum dolor, sit amet consectetur adipisicing elit. Pariatur quidem itaque deserunt. Porro praesentium fugiat explicabo maiores! Laboriosam illo tempora, dicta facere perferendis eligendi exercitationem hic, ut illum iste deserunt."),
                    ], className="feature col"),
                html.Div(children=[
                    html.H3(children=[
                        html.I(className="bi bi-bar-chart me-2"),
                        html.Span(children="Tendencias"),
                        ], className="fs-2 text-body-emphasis"),
                    html.P(children="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Assumenda consequuntur repellendus sit necessitatibus reiciendis aspernatur perferendis consequatur debitis, voluptas eius minus, adipisci omnis porro aperiam quia, tempora sequi! Repellendus, nesciunt."),
                    ], className="feature col"),
                html.Div(children=[
                    html.H3(children=[
                        html.I(className="bi bi-clock me-2"),
                        html.Span(children="Tiempo invertido"),
                        ], className="fs-2 text-body-emphasis"),
                    html.P(children="Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur cum eveniet et sed, deleniti nostrum esse placeat enim saepe omnis consequatur libero nulla expedita neque eos reprehenderit quasi doloremque deserunt."),
                    ], className="feature col"),
                ], className="row g-4 py-5 row-cols-1 row-cols-lg-3"),
            ], className="container px-4 py-5", id="featured-3"),
        ]
)
