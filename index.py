from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from argumentStore.routes.argument import argument
from argumentStore.routes.topic import topic




origins = [
    "http://localhost:4200",
]



tags_metadata = [
    {
        "name": "arguments",
        "description": "Operations with Arguments."
    },
    {
        "name": "topics",
        "description": "Operations with Topics."
    }
]

app = FastAPI(title="ArgumentStore", openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(argument, tags=["arguments"])
app.include_router(topic, tags=["topics"])


@app.get("/")
async def main():
    return {"message": "Hello World"}