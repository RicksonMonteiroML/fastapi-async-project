from fastapi import FastAPI, APIRouter
from views import user_router, assets_router
import uvicorn


app = FastAPI()
router = APIRouter()


app.include_router(user_router)
app.include_router(assets_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, lifespan="auto")