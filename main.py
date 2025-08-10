from fastapi import FastAPI
from pydantic import BaseModel
from rag.rag_chain import create_rag_chain

# Initialize FastAPI app
app = FastAPI()

# Create the RAG chain instance
rag_chain = create_rag_chain()

class Query(BaseModel):
    query: str

@app.post("/recommendations")
async def get_recommendations(query: Query):
    """
    API endpoint to get college recommendations based on a user query.
    """
    response = rag_chain.invoke({"input": query.query})
    return {"response": response["answer"]}

@app.get("/")
async def root():
    return {"message": "College Recommendation API is running. Use the /recommendations endpoint."}
