from fastapi import FastAPI
app = FastAPI()


from swagger_server.routes.topic import topic
app.include_router(topic)

@app.get("/")
async def root():
    return {"message": "Hello World"}
