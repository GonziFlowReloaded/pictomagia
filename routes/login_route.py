from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
from db.connector import get_db

load_dotenv()


router = APIRouter()
# router.mount("/static", StaticFiles(directory="static"), name="static")

url_base = os.getenv("URL_BASE")

@router.get("/login", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "url_base": url_base})

from fastapi import Response

@router.post("/login")
async def login_user(request: Request, email: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    from models.user_model import User
    user = db.query(User).filter(User.email == email, User.contrasena == password).first()
    
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "url_base": url_base, "error": "*Usuario o contraseña incorrectos"})
    
    response = templates.TemplateResponse("home.html", {"request": request, "url_base": url_base})
    #Hacer que la cookie "session" guarde el valor del id del usuario

    response.set_cookie(key="session", value=str(user.id))
    print(response.headers)
    print(user.id)
    response.headers["Location"] = "/home"
    response.status_code = 302
    return response
