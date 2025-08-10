# College Recommendation RAG System 🎓

This project is a Retrieval-Augmented Generation (RAG) system built with FastAPI and LangChain to provide college recommendations based on user queries. It uses a custom dataset of Indian colleges as its knowledge base and leverages a vector database for efficient semantic search.

---

### Features

-   **API Endpoint:** A simple and intuitive API to get college recommendations.
-   **RAG Architecture:** Combines a semantic search (retrieval) with a Large Language Model (generation) to provide factual, context-aware answers.
-   **Custom Knowledge Base:** Uses a CSV file of college data to ground its responses, preventing hallucinations.
-   **Persistent Vector Store:** Utilizes ChromaDB to store and retrieve college data efficiently.
-   **FastAPI Backend:** A lightweight and modern web framework for building the API.

---

### Getting Started

Follow these steps to set up and run the project locally.

#### Prerequisites

-   **Python 3.10+:** Ensure you have a compatible Python version installed.
-   **Conda:** For easy virtual environment management.

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    conda create --name rag_venv python=3.10
    conda activate rag_venv
    ```

3.  **Install dependencies:**
    Install the packages with the following command:
    ```bash
    pip install -r requirements.txt
    ```

---

### Usage

#### 1. Ingest Data

The `ingest.py` script reads the college data from `data.csv`, converts it into embeddings, and stores it in the ChromaDB vector store. You must run this script once to populate the database.

```bash
python ingest.py
```

#### 2. Start the FastAPI Server
Once the data is ingested, you can start the API server.


```bash
uvicorn main:app --reload
```
You will see a message indicating the server is running on ```http://127.0.0.1:8000.```

#### 3. Send a Request
The main endpoint is /recommendations which accepts a POST request. You can use a tool like Postman or a command-line utility to interact with it.

**Example** POST Request (using cURL):

```bash

curl -X POST "[http://127.0.0.1:8000/recommendations](http://127.0.0.1:8000/recommendations)" \
-H "Content-Type: application/json" \
-d '{
  "query": "Suggest an MBA college in Bangalore with high placement and low fee."
}'

```
The API will return a JSON response with a recommendation based on your query.
<br>
You can use ``Postman`` too, for testing the API.

## Project Structure

-   `main.py`: The entry point for the FastAPI application, defining the API endpoints.
-   `ingest.py`: Script to read `data.csv` and populate the vector store.
-   `rag/rag_chain.py`: Contains the logic for building the RAG pipeline using LangChain.
-   `database/vector_store.py`: Defines the custom embedding function and initializes the ChromaDB client.
-   `models/embedding_model.py`: Handles the loading of the Sentence Transformer model.
-   `data.csv`: The knowledge base containing all the college information.
-   `chroma_db/`: The directory where the persistent ChromaDB vector store is stored.


## Troubleshooting

-   **`ModuleNotFoundError`**: Ensure you have activated your `rag_venv` environment and run `pip install -r requirements.txt`.
-   **`AttributeError`**: This often points to a version incompatibility or an incorrect method call. Follow the provided code fixes to ensure your custom classes and methods are compatible with LangChain.
-   **Mixed Data in Response**: If you've ingested data multiple times, your vector store may contain duplicates. Delete the `chroma_db` directory and re-run `python ingest.py` to start with a fresh database.