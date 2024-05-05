from fastapi import APIRouter, HTTPException, Depends, Form, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from db.connector import get_db
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv
from models.user_model import User
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from db.connector import get_db
import os

load_dotenv()


router = APIRouter()
# router.mount("/static", StaticFiles(directory="static"), name="static")

url_base = os.getenv("URL_BASE")

@router.get("/register", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "url_base": url_base})

# Aca se crean los sueños, se que cometí crimenes de guerra en este codigo, pero no me juzguen, era la forma mas rapida de hacerlo
@router.post("/register")
async def register_user(request: Request, email: str = Form(...), password1: str = Form(...), password2: str = Form(...), birthdate= Form(...), profile_picture: UploadFile = File(...), db: Session = Depends(get_db)):
    if password1 != password2:
        return templates.TemplateResponse("register.html", {"request": request, "url_base": url_base, "error": "*Las contraseñas no coinciden "})
    if db.query(User).filter(User.email == email).first():
        return templates.TemplateResponse("register.html", {"request": request, "url_base": url_base, "error": "*El usuario ya existe"})
    
    #Guardar imagen
    


    ruta_directorio = os.path.join(os.getcwd(), "static/users")

    ruta_img = os.path.join(ruta_directorio, "profile_picture_" + email + ".png")
    with open(ruta_img, "wb") as buffer:
        buffer.write(profile_picture.file.read())


    img = "profile_picture_" + email + ".png"


    
    
    user = User(email=email, contrasena=password1, birthdate=birthdate, img=img)
    
    db.add(user)
    db.commit()
    
    return templates.TemplateResponse("login.html", {"request": request, "url_base": url_base, "message": "Usuario creado correctamente!"})
    
    