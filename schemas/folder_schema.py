from pydantic import BaseModel

class CarpetaBase(BaseModel):
    ruta_pictograma: str
    nombre_carpeta: str
    ruta_imagen_carpeta: str = 'folder_image.png'

class CarpetaCreate(CarpetaBase):
    pass