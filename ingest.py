import pandas as pd
import chromadb
from database.vector_store import SentenceTransformerEmbeddingFunction
from langchain_community.vectorstores import Chroma

def ingest_data(file_path: str, collection_name: str = "college_recommendations"):
    """
    Ingests data from a CSV file, creates descriptive strings,
    and stores them in a ChromaDB collection using LangChain.
    """
    df = pd.read_csv(file_path)

    documents = []
    metadatas = []

    for _, row in df.iterrows():
        description = (
            f"{row['name']}, a {row['type']} college in {row['city']}, "
            f"offering a {row['course']} course. "
            f"The average fees are ₹{row['fees']} and the average placement package is ₹{row['avg_package']}. "
            f"It has a ranking of {row['ranking']} and accepts the {row['exam']} exam."
        )
        
        documents.append(description)
        metadatas.append(row.to_dict())
    
    # Use LangChain's Chroma.from_texts to handle embedding and storing
    vector_store = Chroma.from_texts(
        texts=documents,
        embedding=SentenceTransformerEmbeddingFunction(),
        metadatas=metadatas,
        client=chromadb.PersistentClient(path="./chroma_db"),
        collection_name=collection_name
    )

    print(f"Ingestion complete. {len(documents)} colleges added to the collection.")

if __name__ == "__main__":
    ingest_data("data/small_data.csv")