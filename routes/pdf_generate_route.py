from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from jinja2 import Template
router = APIRouter()





@router.post("/pdf_generate", response_class=FileResponse)
def generate_pdf(request: Request, nombre_nene: str = Form(" "), ruta_img: str = Form(...), ruta_pictograma: str = Form(...)):
    print(nombre_nene)

    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pictomagia</title>
        <!-- Integrar Tailwind CSS -->
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="static/css/pictograma_gen.css">

    </head>
    <body>
        <div class="div-padre">
            <form class="card shadow-md rounded-lg p-6" style="border: 3px solid black;">
        <div class="div-imagen-input">
            {% if nombre_nene %}
                <p class="text-center text-2xl font-bold">{{ nombre_nene }}</p>
            {% endif %}

            <div class="div-imagen">
                <img src="{{ ruta_img }}" alt="jeta_nene" class="imagen-jeta">
            </div>
        </div>
        <img src="{{ ruta_pictograma }}" alt="Pictograma" class="pictograma">
    </form>

            
        </div>

        
    </body>
    </html>

    """




    template = Template(html_template)


    html_code = template.render(ruta_img="static/users/"+ruta_img, ruta_pictograma="static/"+ruta_pictograma, nombre_nene=nombre_nene)

    # print(html_code)
    #Guardar html en un archivo
    with open("out.html", "w", encoding="utf-8") as file:
        file.write(html_code)

    from pyhtml2pdf import converter
    converter.convert(r'file:///C:/Users/gonza/Desktop/repopepo/si%20el%20infierno%20existe%20es%20este%20tp/out.html', "pictograma.pdf")
    
    return FileResponse("pictograma.pdf", media_type='application/pdf', filename="pictograma.pdf")

