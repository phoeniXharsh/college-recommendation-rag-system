from sentence_transformers import SentenceTransformer

def get_embedding_model():
    """Initializes and returns the SentenceTransformer embedding model."""
    return SentenceTransformer("all-MiniLM-L6-v2")