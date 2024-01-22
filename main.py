from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
    