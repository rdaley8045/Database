import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import Settings
from api.routers import queues

settings = Settings()

app = FastAPI(title='GWEX2',
              root_path=settings.root_path,
              version=settings.version)

origins = [
    'http://localhost:3000'
]

# allow requests from the localhost front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add routes
app.include_router(queues.router)


if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=5000, reload=True)
