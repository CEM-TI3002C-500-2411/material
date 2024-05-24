from html_to_dash import parse_html

with open("encabezado.html", "r", encoding="utf8") as f:
    texto = f.read()

traduccion = parse_html(texto, if_return=True)

with open("encabezado.py", "w", encoding="utf8") as f:
    f.write(traduccion)