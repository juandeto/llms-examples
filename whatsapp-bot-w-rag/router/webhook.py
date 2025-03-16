from fastapi import APIRouter, Request, Response, status
import os


router = APIRouter(
    prefix="/webhook",
    tags=["meta webhook"]
)

meta_whatsapp_token = os.getenv("META_TOKEN")

@router.get("/")
async def verify_webhook(request: Request):
    # Parámetros que envía Meta
    hub_mode = request.query_params.get("hub.mode")
    hub_token = request.query_params.get("hub.verify_token")
    hub_challenge = request.query_params.get("hub.challenge")

    # Verifica el token (debe coincidir con el que configures en Meta)
    if hub_mode == "subscribe" and hub_token == meta_whatsapp_token:
        return Response(content=hub_challenge, media_type="text/plain", status_code=status.HTTP_200_OK)
    else:
        return Response(content="Verification failed", status_code=status.HTTP_401_UNAUTHORIZED)


# Ruta para recibir mensajes (Meta enviará un POST aquí)
@router.post("/")
async def receive_message(request: Request):
    data = await request.json()
    print("Mensaje recibido:", data)  # Aquí procesarás el mensaje
    return {"status": "ok"}