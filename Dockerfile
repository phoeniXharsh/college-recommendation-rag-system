# Use an official lightweight Python image as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application code, including the pre-built chroma_db
COPY . .

# Expose the port on which the app will run
EXPOSE 8080

# The command to run the application
# Removed ingest.py from build - data should be pre-ingested
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]