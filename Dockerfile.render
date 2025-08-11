# Multi-stage Docker build for Render (512MB limit)
# Stage 1: Build environment with all dependencies
FROM python:3.10-slim as builder

# Set build environment variables
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install all dependencies
COPY requirements.render.txt requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime environment (minimal)
FROM python:3.10-slim as runtime

# Set runtime environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH=/root/.local/bin:$PATH

# Install only runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python packages from builder stage
COPY --from=builder /root/.local /root/.local

# Copy application code (only essential files)
COPY main.py .
COPY startup.py .
COPY rag/ ./rag/
COPY database/ ./database/
COPY models/ ./models/
COPY data/ ./data/
COPY chroma_db/ ./chroma_db/
# .env file not copied - use environment variables from platform

# Use environment variable for port (Render requirement)
EXPOSE $PORT

# Command to run the application
CMD uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1
