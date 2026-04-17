FROM python:3.11-slim

WORKDIR /app

# Prevent Python issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Railway will override internally)
EXPOSE 8000

# Start server (IMPORTANT: use Railway PORT)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
