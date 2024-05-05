from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
from starlette.staticfiles import StaticFiles
from middleware.auth_cookie import auth_cookie


router = APIRouter()
router.mount("/static", StaticFiles(directory="static"), name="static")



@router.get("/logout", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request):
    #Borrar la cookie "session"
    response = templates.TemplateResponse("index.html", {"request": request})
    response.delete_cookie(key="session")
    response.delete_cookie(key="ruta")
    
    return response
