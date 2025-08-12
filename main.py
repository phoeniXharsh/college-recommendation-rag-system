from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from rag.rag_chain import create_rag_chain

# Initialize FastAPI app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create the RAG chain instance
rag_chain = create_rag_chain()

class Query(BaseModel):
    query: str

@app.get("/")
async def root():
    """
    Serve the main HTML interface
    """
    return FileResponse('static/index.html')

@app.post("/recommendations")
async def get_recommendations(query: Query):
    """
    API endpoint to get college recommendations based on a user query.
    """
    response = rag_chain.invoke({"input": query.query})
    return {"response": response["answer"]}
