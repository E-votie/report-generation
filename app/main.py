from fastapi import FastAPI
from api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Bot Service")
app.include_router(chat_router, tags=["Chat API"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World!"}
