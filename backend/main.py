# import uvicorn
from fastapi import FastAPI
from users.views import router as users_router

app = FastAPI(title="Запись", summary="API для записи, на прием", debug=True)
app.include_router(users_router)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
