import json
from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/jobs")
def get_jobs():
    with open("jobs.json") as f:
        jobs = json.load(f)
        return jobs

if __name__=="__main__":
    uvicorn.run(app,port=9000)

