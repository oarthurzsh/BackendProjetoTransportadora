from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.core.database import get_db
from .service import FreteService
from .schema import FreteCreate

router = APIRouter(prefix="/fretes", tags=["fretes"])
templates = Jinja2Templates(directory="templates")

@router.get("/cadastrar")
def view_cadastrar(request: Request):
    return templates.TemplateResponse("cadastrar_frete.html", {"request": request})

@router.post("/cadastrar")
def do_cadastrar(
    request: Request,
    destino: str = Form(...),
    peso: float = Form(...),
    transportadora: str = Form(...),
    db: Session = Depends(get_db)
):
    service = FreteService(db)
    service.create_frete(FreteCreate(destino=destino, peso=peso, transportadora=transportadora))
    return RedirectResponse(url="/fretes", status_code=303)

@router.get("/")
def list_all(request: Request, db: Session = Depends(get_db)):
    service = FreteService(db)
    fretes = service.list_fretes()
    return templates.TemplateResponse("listar_fretes.html", {"request": request, "fretes": fretes})
