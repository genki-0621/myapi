cat > main.py <<'PY'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=[os.environ.get("ALLOW_ORIGIN","*")],
    allow_methods=["*"], allow_headers=["*"])
@app.get("/healthz") 
def health(): 
    return {"ok": True}
@app.get("/hello")   
def hello(name: str="world"): 
    return {"msg": f"hello {name}"}
PY
