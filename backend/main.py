from fastapi import FastAPI

from users.views import router as users_router
from services.views import router as services_router
from specializations.views import router as specializations_router
from specialists.views import router_profile, router as specialists_router

from records.views import router as records_router

app = FastAPI(title="Запись", summary="API для регистрации записи")

app.include_router(records_router)
app.include_router(specialists_router)
app.include_router(router_profile)
app.include_router(services_router)
app.include_router(specializations_router)
app.include_router(users_router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
