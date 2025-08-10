import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from database.vector_store import get_chroma_collection
# from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

def create_rag_chain():
    """
    Creates and returns the RAG pipeline using LangChain.
    """
    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    # Get the LangChain Chroma vector store and create a retriever
    vector_store = get_chroma_collection()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Define the new, improved prompt template
    prompt_template = PromptTemplate.from_template(
        """
        You are a helpful AI assistant that recommends colleges based on user queries.
        You must provide a clear and readable response using only the information from the provided context.
        Do not use tables or complex formatting. Use a conversational tone and bullet points.

        Instructions:
        1. Begin with a concise summary based on the user's request and the top 3 retrieved colleges.
        2. List the top college matches using bullet points. For each college, include its name, fee, average placement package, and type.
        3. Clearly state a final recommendation based on the user's preferences.
        4. If you cannot find a college in the exact city mentioned, but you find a college in a geographically nearby city, you can mention that as a possible alternative.
        5. If the context does not contain any relevant information, state that you cannot provide a recommendation.

        Context:
        {context}

        Question: {input}
        """
    )

    # Create the document chain
    document_chain = create_stuff_documents_chain(llm, prompt_template)
    
    # Create the RAG chain
    rag_chain = create_retrieval_chain(retriever, document_chain)
    
    return rag_chain