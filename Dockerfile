FROM python:3.14-slim

# Set working dir
WORKDIR /app

# Install system dependencies required for Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        git \
        zlib1g-dev \
        libjpeg-dev \
        libglib2.0-0 \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install packages
COPY requirements.txt ./
RUN python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Expose default Streamlit port
EXPOSE 8501

# Streamlit configuration
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV PORT=8501

# Default command uses Render's PORT environment variable
CMD ["sh", "-c", "python -m streamlit run Welcome.py --server.port ${PORT} --server.address 0.0.0.0"]
