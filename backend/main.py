from fastapi import FastAPI
from users.views import router as users_router

app = FastAPI(title="Запись", summary="API для записи, на прием")
app.include_router(users_router)
