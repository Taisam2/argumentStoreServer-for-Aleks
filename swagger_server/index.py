from fastapi import FastAPI
app = FastAPI()


from routes.topic import topic
app.include_router(topic)

@app.get("/")
async def root():
    return {"message": "Hello World"}
