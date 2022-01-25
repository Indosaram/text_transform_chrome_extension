"Main app"


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Text(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def get():
    return "<h1>Hello World</h1>"


@app.post("/text")
def main(request: Text) -> Text:
    return {"text": request.text}


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
