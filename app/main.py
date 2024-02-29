from fastapi import FastAPI
import os
#from dotenv import load_dotenv

#load_dotenv()
app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hello World {os.getenv('test1')}"}
