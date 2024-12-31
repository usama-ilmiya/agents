FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for librosa
RUN apt-get update && apt-get install -y \
    ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
# Define the command to run when the container starts
CMD ["uvicorn", "pra.main:app", "--timeout-keep-alive", "0", "--host", "0.0.0.0", "--port", "8080"]
#ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
