from fastapi import FastAPI
from pydantic import BaseModel
from rag.rag_chain import create_rag_chain
from startup import check_and_ingest_data

# Initialize FastAPI app
app = FastAPI()

# Check and ingest data if needed (runs once at startup)
check_and_ingest_data()

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
