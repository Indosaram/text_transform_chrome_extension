"Main app"


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from abstractive_summarizer import abstractive_summarizer
from extractive_summarizer import extractive_summarizer
from keyword_extraction import keyword_extraction


class Text(BaseModel):
    text: str


class Summary(BaseModel):
    keywords: str
    abs_summary: str
    ext_summary: str


app = FastAPI()


@app.get("/")
def get():
    return "<h1>Hello World</h1>"


@app.post("/text")
def main(request: Text) -> Text:
    # TODO: Split into subprocesses
    abs_summary = abstractive_summarizer(request.text)
    ext_summary = extractive_summarizer(request.text)
    keywords = keyword_extraction(request.text)
    return {
        "keywords": keywords,
        "abs_summary": abs_summary,
        "ext_summary": ext_summary,
    }


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
