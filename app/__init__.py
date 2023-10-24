from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from .routes.products import router as Router

app = FastAPI(
    title="Shopping Cart",
    description="Shopping Cart Application",
)

app.include_router(Router, tags=["Products"], prefix="/products")


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/")
async def read_root():
    return "App Started Successfully"
