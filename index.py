from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from argument_store.routes.argument import argument
from argument_store.routes.topic import topic

origins = ["*"]
#     "https://argument-store-client.azurewebsites.net/",
#     "https://argument-store-client.azurewebsites.net/topics",
#     "https://argument-store-client.azurewebsites.net/arguments",


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
    return {"message": "Server is running."}