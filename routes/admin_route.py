from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
import httpx
from starlette.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db.connector import get_db
# from middleware.auth_cookie import AuthCookie
from middleware.auth_cookie import auth_cookie
from dotenv import load_dotenv
from models.personal_folder_model import CarpetaPersonal
from models.general_folder_model import CarpetaGeneral
from models.user_model import User
from models.usuarios_carpetas_personales_model import UsuariosCarpetasPersonales

import os

load_dotenv()

URL_BASE = os.getenv("URL_BASE")

router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get("/admin", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request):

    return templates.TemplateResponse("admin.html", {"request": request, "url_base": URL_BASE})


@router.get("/admin/general", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request, db: Session = Depends(get_db)):

    #Hacer una peticion get a la ruta /carpeta_general
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/carpeta_general", timeout=10)
        carpetas = response.json()

    print(carpetas)

    return templates.TemplateResponse("admin_general.html", {"request": request, "carpetas": carpetas})

@router.get("/admin/personalizadas", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request, db: Session = Depends(get_db)):
    
    carpetas = db.query(CarpetaPersonal).all()
    usuarios = db.query(User).all()
    carpetas_data = []
    usuarios_data = []
    for carpeta in carpetas:
        carpetas_data.append(carpeta.__dict__)
    for usuario in usuarios:
        usuarios_data.append(usuario.__dict__)

    for carpeta in carpetas_data:
        carpeta["usuarios"] = []
        for usuario in usuarios_data:
            usuario_carpeta = db.query(UsuariosCarpetasPersonales).filter(
                UsuariosCarpetasPersonales.usuario_id == usuario["id"],
                UsuariosCarpetasPersonales.carpeta_personal_id == carpeta["id"]
            ).first()
            if usuario_carpeta:
                carpeta["usuarios"].append(usuario)


    


    return templates.TemplateResponse("admin_personal.html", {"request": request, "carpetas": carpetas_data, "usuarios": usuarios_data})


