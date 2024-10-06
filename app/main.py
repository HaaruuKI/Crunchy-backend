from fastapi import FastAPI
from app.routers import aws

app = FastAPI()

app.include_router(aws.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
