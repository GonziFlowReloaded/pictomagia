from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from starlette.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from models.user_model import User
from db.connector import get_db
from middleware.auth_cookie import auth_cookie


router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/pictogramas/{i}", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request, i: str, db: Session = Depends(get_db)):
    print(i)
    #Obtener id del usuario mediante la cookie "session"
    id_usuario = request.cookies.get("session")
    print(id_usuario)

    #Obtener usuario mediante el id
    usuario = db.query(User).filter(User.id == id_usuario).first()

    ruta_img = usuario.img
    return templates.TemplateResponse("pictograma_template.html", {"request": request, "nombre_seccion": "Pictograma", "ruta_pictograma": "pictogramas/"+str(i)+".png", 'ruta_anterior': request.cookies.get("ruta"),
                                                                   "ruta_img": ruta_img,
                                                                   })
