from reactpy import component, html, run
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos


@component
def App():
    return html.div(
        html.h1("Hola Mundo"),
        html.h2("Lista de Productos"),
        html.ul([html.li(producto["nombre"]) for producto in productos]),
    )


app = Flask(__name__)
configure(app, App)  # Configura la aplicación Flask para usar ReactPy
app.run(host="0.0.0.0", debug=True)  # Ejecuta la aplicación Flask en el puerto 5000
