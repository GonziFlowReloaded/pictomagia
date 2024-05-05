from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    contrasena = Column(String)
    birthdate = Column(String)
    tipo_usuario_id = Column(Integer, default=2)
    img = Column(String, default="default-photo.png")


