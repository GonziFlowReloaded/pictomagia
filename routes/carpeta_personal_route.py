from fastapi import APIRouter, HTTPException, Depends, Form, Request, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from db.connector import get_db
from models.personal_folder_model import CarpetaPersonal
from models.usuarios_carpetas_personales_model import UsuariosCarpetasPersonales
from models.user_model import User
import os

router = APIRouter()

@router.get("/carpeta_personal")
async def read_items(request: Request, db: Session = Depends(get_db)):
    carpetas = db.query(CarpetaPersonal).all()
    return carpetas

@router.post("/carpeta_personal")
async def create_item(nombre: str = Form(...), pictograma: UploadFile = File(...), db: Session = Depends(get_db)):
    carpeta = CarpetaPersonal(nombre_carpeta=nombre)
    

    pictograma_path = f"static/pictogramas/p-{carpeta.nombre_carpeta}.png"
    with open(pictograma_path, "wb") as buffer:
        buffer.write(pictograma.file.read())
    carpeta.ruta_pictograma = f"/pictogramas/p-{carpeta.nombre_carpeta}"
    
    # usuario_carpeta_personal = UsuariosCarpetasPersonales(usuario_id=usuario_id, carpeta_personal_id=carpeta.nombre_carpeta)
    # db.add(usuario_carpeta_personal)
    # db.commit()
    db.add(carpeta)
    db.commit()
    

    return RedirectResponse(url="/admin/personalizadas", status_code=303)

@router.post("/carpeta_personal/{id}")
async def update_or_delete_item(request: Request, id: int, db: Session = Depends(get_db), nombre: str = Form(None), pictograma: UploadFile = File(None), http_method: str = Form(...)):
    carpeta = db.query(CarpetaPersonal).filter(CarpetaPersonal.id == id).first()
    if not carpeta:
        raise HTTPException(status_code=404, detail="Carpeta no encontrada")

    if http_method == "PUT":
        if pictograma:
            pictograma_path = f"static/pictogramas/p-{carpeta.nombre_carpeta}.png"
            with open(pictograma_path, "wb") as buffer:
                buffer.write(pictograma.file.read())
            carpeta.ruta_pictograma = f"/pictogramas/p-{carpeta.nombre_carpeta}"

        if nombre:
            carpeta.nombre_carpeta = nombre

        db.commit()
        return RedirectResponse(url="/admin/personalizadas", status_code=303)
    elif http_method == "DELETE":
        try:
            if carpeta.ruta_pictograma:
                total_path = os.getcwd() + "/static" + carpeta.ruta_pictograma + ".png"
                os.remove(total_path)
        except Exception as e:
            print(f"Error deleting file: {e}")

        db.query(UsuariosCarpetasPersonales).filter(UsuariosCarpetasPersonales.carpeta_personal_id == carpeta.id).delete()
        db.delete(carpeta)
        db.commit()
        return RedirectResponse(url="/admin/personalizadas", status_code=303)
    else:
        raise HTTPException(status_code=400, detail="Método no soportado")
