from fastapi import APIRouter, HTTPException, Depends, Form, Request, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from db.connector import get_db
from models.general_folder_model import CarpetaGeneral
import os


router = APIRouter()

@router.get("/carpeta_general")
async def read_item(request: Request, db: Session = Depends(get_db)):
    carpetas = db.query(CarpetaGeneral).all()
    return carpetas


@router.post("/carpeta_general")
async def create_item(nombre: str = Form(...), pictograma: UploadFile = File(...), db: Session = Depends(get_db)):
    carpeta = CarpetaGeneral(nombre_carpeta=nombre)
    #Obtener carpeta con el id generado
    

    with open(f"static/pictogramas/{carpeta.nombre_carpeta}.png", "wb") as buffer:
        buffer.write(pictograma.file.read())
    carpeta.ruta_pictograma = f"/pictogramas/{carpeta.nombre_carpeta}"
    db.add(carpeta)
    db.commit()
    return RedirectResponse(url="/admin/general", status_code=303)

@router.post("/carpeta_general/{id}")
async def update_or_delete_item(request: Request, id: int, db: Session = Depends(get_db), nombre: str = Form(None), pictograma: UploadFile = File(None), http_method: str = Form(...)):
    carpeta = db.query(CarpetaGeneral).filter(CarpetaGeneral.id == id).first()
    if not carpeta:
        raise HTTPException(status_code=404, detail="Carpeta no encontrada")

    if http_method == "PUT":
        print("PUT")
        print(nombre)
        print(pictograma)
        if pictograma.size is not 0:
            print("Entre a pictograma")
            with open(f"static/pictogramas/{carpeta.nombre_carpeta}.png", "wb") as buffer:
                buffer.write(pictograma.file.read())
            carpeta.ruta_pictograma = f"/pictogramas/{carpeta.nombre_carpeta}"

        if nombre:
            carpeta.nombre_carpeta = nombre

        print(carpeta.nombre_carpeta)
        print(carpeta.ruta_pictograma)

        db.commit()
        return RedirectResponse(url="/admin/general", status_code=303)
    elif http_method == "DELETE":
        print("DELETE")
        # Eliminar el pictograma
        try:
            if carpeta.ruta_pictograma:
                total_path = os.getcwd() + "/static" + carpeta.ruta_pictograma + ".png"
                os.remove(total_path)
        except Exception as e:
            print(f"Error deleting file: {e}")


        
        db.delete(carpeta)
        db.commit()

        return RedirectResponse(url="/admin/general", status_code=303)
    else:
        raise HTTPException(status_code=400, detail="Método no soportado")
    


"""@router.post("/carpeta_general")
async def create_item(request: Request, nombre: str = Form(...), pictograma = File(...), db: Session = Depends(get_db)):
    
    with open("static/pictogramas/"+nombre+".png", "wb") as buffer:
        buffer.write(pictograma.file.read())
    carpeta = CarpetaGeneral(nombre=nombre, img="/pictogramas/"+nombre+".png")
    db.add(carpeta)
    db.commit()
    return carpeta

@router.put("/carpeta_general/{id}")
async def update_item(request: Request, id: int, nombre: str = Form(...), pictograma = File(...), db: Session = Depends(get_db)):
    carpeta = db.query(CarpetaGeneral).filter(CarpetaGeneral.id == id).first()
    with open("static/pictogramas/"+nombre+".png", "wb") as buffer:
        buffer.write(pictograma.file.read())
    carpeta.nombre = nombre
    carpeta.img = "/pictogramas/"+nombre+".png"
    db.commit()
    return carpeta

@router.delete("/carpeta_general/{id}")
async def delete_item(request: Request, id: int, db: Session = Depends(get_db)):
    carpeta = db.query(CarpetaGeneral).filter(CarpetaGeneral.id == id).first()
    db.delete(carpeta)
    db.commit()
    return carpeta"""
