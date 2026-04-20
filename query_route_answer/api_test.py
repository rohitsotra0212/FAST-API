from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

data_items = [
    {
    "query":"What is GEN AI",
    "route": "WEB",
    "answer":"GEN AI is AI sub-parts"
    },
    {
    "query":"What is date of services",
    "route": "RAG",
    "answer":"date of service is 12-07-2019"
    },
    {
    "query":"What is 10*100?",
    "route": "WEB",
    "answer":"10*100 is 1000"
    },
    {
    "query":"What is Full Form of RAG?",
    "route": "WEB",
    "answer":"Retrieval Augemented Generation"
    }
]

class ResponseSchema(BaseModel):
    query: str
    route: str
    answer: str

@app.get('/')
def home():
    return {"message":"FastAPI is Running"}

@app.post('/save')
def save(data: ResponseSchema):
    items = data.model_dump()
    data_items.append(items)
    return{
        "message":"Data Saved",
        "status": "success",
        "data": data_items,
        "total_saved": len(data_items)
    }

@app.get('/all')
def get_all():
    return {
        "count": len(data_items),
        "items": data_items
    } 

@app.get('/all/filtered/route/web')
def get_web_route():
    filtered_data = [items for items in data_items if items["route"].upper() == "WEB"]

    return{
        "total_rows": len(filtered_data),
        "items": filtered_data
    }

@app.get('/all/filtered/route/rag')
def get_rag_route():
    filtered_data = [items for items in data_items if items["route"].upper() == "RAG"]

    return{
        "total_rows": len(filtered_data),
        "items": filtered_data
    }

if __name__ == "__main__":
    uvicorn.run("api_test:app", host="127.0.0.1", port=8000, reload=True)