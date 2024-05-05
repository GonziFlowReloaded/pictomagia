from fastapi import APIRouter, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")
# from middleware.auth_cookie import AuthCookie
from middleware.auth_cookie import auth_cookie

router = APIRouter()



@router.get("/home", response_class=HTMLResponse, dependencies=[Depends(auth_cookie)])
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})