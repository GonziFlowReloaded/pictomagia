from fastapi import APIRouter, Request, Form, File
from fastapi.responses import FileResponse
import pdfkit
import tempfile

router = APIRouter()



@router.post("/download")
def download_pdf(html: str = Form(...)):
    # Convertir el HTML a PDF
    print("hola")
    print(html)
    
    pdf = pdfkit.from_string(html, configuration=pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"), options={"encoding": "UTF-8"}, css="notebooks\pictograma.css")
    
    # Crear un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf)
        tmp.close()
        return FileResponse(tmp.name, filename="pictograma.pdf", media_type="application/pdf")


