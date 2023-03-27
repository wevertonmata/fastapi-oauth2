from fastapi import APIRouter

from .endpoints import artigo, usuario


api_router_v1 = APIRouter()
api_router_v1.include_router(artigo.router, tags=['artigos'], prefix="/artigos")
api_router_v1.include_router(usuario.router, tags=['usuarios'], prefix="/usuarios")