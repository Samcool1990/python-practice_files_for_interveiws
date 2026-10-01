from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],   
)

class custom_exception(Exception):
    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message

@app.exception_handler(custom_exception)
async def custom_exception_handler(request: Request, exc: custom_exception):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a custom exception: {exc.message}"},
    )

@app.get("/")
def read_root():
    return {"Hello": "World"}

