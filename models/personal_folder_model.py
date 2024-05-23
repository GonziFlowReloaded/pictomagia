from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CarpetaPersonal(Base):
    __tablename__ = 'carpeta_personal'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_pictograma = Column(String(255), nullable=False)
    nombre_carpeta = Column(String(100), nullable=False)
    ruta_imagen_carpeta = Column(String(255), default='folder_image.png')