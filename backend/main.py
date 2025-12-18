from fastapi import FastAPI
from pydantic import BaseModel
from agent import invoke_agent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ADD THESE 3 LINES:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # or ["http://127.0.0.1"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI(title="Weather Agent API")

class Query(BaseModel):
    input: str

@app.get("/")
async def root():
    return {"message": "Weather Agent API running"}

@app.post("/chat")
async def chat(query: Query):
    response = await invoke_agent(query.input)
    return {"response": response}
