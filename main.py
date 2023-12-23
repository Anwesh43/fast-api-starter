from fastapi import FastAPI, Response 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse 
import uvicorn 
app = FastAPI(port=5000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/hello")
def hello(): 
    return HTMLResponse("<div style = 'background:yellow; width: 100px; height: 100px; display: flex; justify-content:center; align-items: center'>Hello</div>")

uvicorn.run(app, host="0.0.0.0", port = 4000)