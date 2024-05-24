import dash
from dash import html

dash.register_page(__name__,
                   path="/",
                   title="Ventas de videojuegos",
                   name="Ventas de videojuegos")

layout = html.Div(children=[
    html.Div(children=[
        html.Div(children=[
            html.Img(src="/assets/images/inicio.jpg",
                     alt="Imagen de inicio con un videojuego",
                     width = 700,
                     height = 500,
                     className="d-block mx-lg-auto img-fluid")
            ], className="col-10 col-sm-8 col-lg-6"),
        html.Div(children=[
            html.H1(children="Análisis de ventas de videojuegos",
                    className="display-5 fw-bold text-body-emphasis lh-1 mb-3"),
            html.P(children="""
                   Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis dolorum assumenda suscipit molestiae! Et eius odio asperiores expedita tenetur cupiditate veritatis labore molestiae omnis ipsa, provident id molestias, nobis quos.
            Perferendis harum, quis mollitia tempore voluptates expedita dolores ad dicta at deserunt iste dolorem. Quibusdam fuga impedit quam provident consectetur vel, tempore qui magnam dignissimos temporibus labore obcaecati! Optio, facilis.
            Laborum culpa cum dolores repellendus debitis veniam provident, quos similique consequuntur quas optio, amet quaerat laboriosam eligendi vitae. Vitae adipisci culpa possimus quibusdam cupiditate aspernatur recusandae quaerat soluta omnis quos?
            Illum, commodi. Pariatur, minus? Esse expedita quaerat sunt magnam quidem, quas quibusdam molestiae? Doloremque tempore repellat porro libero ad, possimus quo minima magnam veniam dolorem dicta praesentium aut. Possimus, vero!
            Repudiandae sequi cumque alias vero sint itaque numquam? Harum ratione sequi laboriosam obcaecati ex recusandae incidunt cumque, consectetur, suscipit, accusantium et esse. Quaerat fugiat autem porro cum laboriosam tempore doloremque!
                   """, className="lead")
            ], className="col-lg-6")
        ], className="row flex-lg-row-reverse align-items-center g-5 py-5 appear")
    ], className="container col-xxl-8 px-4 py-5")