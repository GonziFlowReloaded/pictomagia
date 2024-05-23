from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from db.connector import get_db
from models.usuarios_carpetas_personales_model import UsuariosCarpetasPersonales
from models.user_model import User

router = APIRouter()

@router.post("/usuarios_carpetas_personales/{usuario_id}/{carpeta_id}")
async def delete_user_folder_association(usuario_id: int, carpeta_id: int,  db: Session = Depends(get_db), http_method: str = Form(...)):

    if http_method == "DELETE":
        usuario_carpeta = db.query(UsuariosCarpetasPersonales).filter(
            UsuariosCarpetasPersonales.usuario_id == usuario_id,
            UsuariosCarpetasPersonales.carpeta_personal_id == carpeta_id
        ).first()

        if not usuario_carpeta:
            raise HTTPException(status_code=404, detail="Relación no encontrada")
        
        db.delete(usuario_carpeta)
        db.commit()
        return RedirectResponse(url="/admin/personalizadas", status_code=303)

@router.post("/usuarios_carpetas_personales/{carpeta_id}")
async def create_user_folder_association(
    carpeta_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    # Obtener todos los datos de la solicitud
    data = await request.form()
    http_method = data.get("http_method")
    usuario_id = data.get("usuario_id")

    if http_method == "POST":
        usuario_carpeta = UsuariosCarpetasPersonales(usuario_id=usuario_id, carpeta_personal_id=carpeta_id)
        db.add(usuario_carpeta)
        db.commit()
        return RedirectResponse(url="/admin/personalizadas", status_code=303)

    
    """
    async def create_user_folder_association(usuario_id: int, carpeta_id: int, db: Session = Depends(get_db), http_method: str = Form(...)):
    if http_method == "POST":
        usuario_carpeta = UsuariosCarpetasPersonales(usuario_id=usuario_id, carpeta_personal_id=carpeta_id)
        db.add(usuario_carpeta)
        db.commit()
        return RedirectResponse(url="/admin/personalizadas", status_code=303)
    """