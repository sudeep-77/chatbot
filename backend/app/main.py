from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router
# from .database import init_db

app = FastAPI()

origins = [
    "*",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup():
#     await init_db()

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Chatbot API is running!"}
