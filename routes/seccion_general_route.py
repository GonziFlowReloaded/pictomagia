from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from starlette.staticfiles import StaticFiles
from models.general_folder_model import CarpetaGeneral
from schemas.folder_schema import CarpetaCreate
from sqlalchemy.orm import Session
from db.connector import get_db
from middleware.auth_cookie import auth_cookie


router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/seccion_general", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request, db: Session = Depends(get_db)):

    carpetas = db.query(CarpetaGeneral).all()
    results = []
    for carpeta in carpetas:
        results.append({
            "ruta_pictograma": carpeta.ruta_pictograma,
            "nombre_carpeta": carpeta.nombre_carpeta,
            "ruta_imagen_carpeta": carpeta.ruta_imagen_carpeta
        })
    
    response = templates.TemplateResponse("seccion_template.html", {"request": request, "nombre_seccion": "Rutinas Generales", "carpetas": results})
    response.set_cookie(key="ruta", value="seccion_general")


    return response