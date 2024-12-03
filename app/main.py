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

@app.post("/image")
async def image():
    return {
    "answer": "The current Chairman of the Election Commission of Sri Lanka is Mr. R.M.A.L. Ratnayake. He has extensive experience in the field, having served in various capacities within the Department of Elections and the Election Commission since 1985.",
    "resource": 
        {
        "type": "image",
        "url": "https://elections.gov.lk/web/wp-content/uploads/contact-image/ameer_member.jpg",
        "caption": "Mr. R.M.A.L. Ratnayake"
        }
    }
