from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.get("/status")
def status():
    return {"status": "200"}
