from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.user_model import User
from models.personal_folder_model import CarpetaPersonal

Base = declarative_base()

class UsuariosCarpetasPersonales(Base):
    __tablename__ = 'usuarios_carpetas_personales'

    usuario_id = Column(Integer,  primary_key=True)
    carpeta_personal_id = Column(Integer,  primary_key=True)

    
