from fastapi import Request, HTTPException

async def auth_cookie(request: Request):
    # Aquí colocas la lógica de autenticación de tu middleware
    # Puedes adaptarla de acuerdo a cómo funciona tu middleware AuthCookie
    cookie = request.cookies.get("session")
    if not cookie:
        
        raise HTTPException(status_code=401, detail="Unauthorized")