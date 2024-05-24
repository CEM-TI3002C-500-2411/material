html.Div(
    className="container",
    children=[
        html.Header(
            className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom",
            children=[
                html.A(
                    href="/index.html",
                    className="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none",
                    children=[
                        html.Span(
                            className="fs-4",
                            children=[
                                html.I(className="bi bi-controller me-2"),
                                html.Span(children=["Ventas de videojuegos"]),
                            ],
                        )
                    ],
                ),
                html.Ul(
                    className="nav nav-pills",
                    children=[
                        html.Li(
                            className="nav-item",
                            children=[
                                html.A(
                                    href="/index.html",
                                    className="nav-link active",
                                    **{"aria-current": "page"},
                                    children=["Inicio"]
                                )
                            ],
                        ),
                        html.Li(
                            className="nav-item",
                            children=[
                                html.A(
                                    href="/tablero.html",
                                    className="nav-link",
                                    children=["Tablero"],
                                )
                            ],
                        ),
                        html.Li(
                            className="nav-item",
                            children=[
                                html.A(
                                    href="/hallazgos.html",
                                    className="nav-link",
                                    children=["Hallazgos"],
                                )
                            ],
                        ),
                        html.Li(
                            className="nav-item",
                            children=[
                                html.A(
                                    href="/predicciones.html",
                                    className="nav-link",
                                    children=["Predicciones"],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        )
    ],
)
