#!/usr/bin/env python3
"""
Startup script that checks if data is ingested and runs ingestion if needed.
This runs at application startup instead of during Docker build.
"""
import os
import sys
from pathlib import Path

def check_and_ingest_data():
    """Check if ChromaDB has data, if not, run ingestion."""
    chroma_db_path = Path("./chroma_db")
    
    # Check if ChromaDB directory exists and has data
    if not chroma_db_path.exists() or not any(chroma_db_path.iterdir()):
        print("ChromaDB not found or empty. Running data ingestion...")
        try:
            from ingest import ingest_data
            ingest_data("data/small_data.csv")
            print("Data ingestion completed successfully!")
        except Exception as e:
            print(f"Error during data ingestion: {e}")
            sys.exit(1)
    else:
        print("ChromaDB found with existing data. Skipping ingestion.")

if __name__ == "__main__":
    check_and_ingest_data()
