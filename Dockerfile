# Use an official lightweight Python image as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the working directory
COPY . .

# Ingest data into ChromaDB during the build process
# The chroma_db directory should be committed to your Git repo
RUN python ingest.py

# Expose the port on which the app will run
EXPOSE 8080

# The command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]