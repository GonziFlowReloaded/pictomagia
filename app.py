from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
from starlette.staticfiles import StaticFiles
from routes import login_route, register_route, home_route, seccion_personalizada_route, seccion_general_route, logout_route, pictograma_route, pdf_generate_route, admin_route, carpeta_general_route, carpeta_personal_route, usuarios_carpetas_personales_route



load_dotenv()

url_base = os.getenv("URL_BASE")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(login_route.router)
app.include_router(register_route.router)
app.include_router(home_route.router)
app.include_router(seccion_general_route.router)
app.include_router(seccion_personalizada_route.router)
app.include_router(logout_route.router)
app.include_router(pictograma_route.router)
# app.include_router(download_route.router)
app.include_router(pdf_generate_route.router)
app.include_router(admin_route.router)
app.include_router(carpeta_general_route.router)
app.include_router(carpeta_personal_route.router)
app.include_router(usuarios_carpetas_personales_route.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "url_base": url_base})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)

