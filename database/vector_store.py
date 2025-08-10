import chromadb
from models.embedding_model import get_embedding_model
from chromadb.api.types import EmbeddingFunction, Documents, Embeddings
from langchain_community.vectorstores import Chroma

# A custom EmbeddingFunction class that meets the LangChain interface
class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.embedding_model = get_embedding_model()

    def __call__(self, input: Documents) -> Embeddings:
        return self.embedding_model.encode(input).tolist()
    
    def embed_documents(self, documents: Documents) -> Embeddings:
        """Embeds a list of documents."""
        return self.embedding_model.encode(documents).tolist()

    def embed_query(self, query: str) -> Embeddings:
        """Embeds a single query string."""
        return self.embedding_model.encode([query]).tolist()[0]

def get_chroma_collection(collection_name: str = "college_recommendations"):
    """Initializes and returns the LangChain Chroma vector store."""
    embedding_function = SentenceTransformerEmbeddingFunction()
    
    client = chromadb.PersistentClient(path="./chroma_db")
    
    vector_store = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embedding_function
    )
    return vector_store