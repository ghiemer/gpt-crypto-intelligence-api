# ---- Base image ----
    FROM python:3.11-slim

    # ---- Environment config ----
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    # ---- Working directory ----
    WORKDIR /app
    
    # ---- Install dependencies ----
    COPY requirements.txt .
    RUN pip install --upgrade pip && pip install -r requirements.txt
    
    # ---- Copy project files ----
    COPY . .
    
    # ---- Expose port & start ----
    EXPOSE 10000
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
    