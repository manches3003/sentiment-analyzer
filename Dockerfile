# ---- Stage 1: base image ----
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies first (Docker caches this layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY app/ ./app/

# Expose the port FastAPI will run on
EXPOSE 8000

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]