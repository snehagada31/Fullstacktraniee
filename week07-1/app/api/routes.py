from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    return {
        "message": "Welcome to FastAPI Project Template"
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@router.get("/version")
async def version():
    return {
        "version": "0.1.0"
    }