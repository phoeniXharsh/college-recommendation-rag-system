from sentence_transformers import SentenceTransformer
import os

# Global variable to cache the model
_embedding_model = None

def get_embedding_model():
    """Initializes and returns the SentenceTransformer embedding model with memory optimization."""
    global _embedding_model
    if _embedding_model is None:
        # Use a smaller, more memory-efficient model
        model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
        _embedding_model = SentenceTransformer(model_name)
    return _embedding_model