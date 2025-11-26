# ---- Base Python Image ----
FROM python:3.11-slim

# Prevent Python from buffering stdout
ENV PYTHONUNBUFFERED=1

# Set pythonpath so "src." imports work
ENV PYTHONPATH="/app"

# ---- Work Directory ----
WORKDIR /app

# ---- Copy Requirement First (for Docker caching) ----
COPY requirements.txt .

# ---- Install Dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy Full Project ----
COPY . .

# ---- Expose FastAPI Port ----
EXPOSE 8000

# ---- Run FastAPI Server ----
# Adjust "main:app" if your FastAPI app is in src/main.py -> use "src.main:app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
