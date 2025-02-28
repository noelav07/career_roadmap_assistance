FROM python:3.12-slim

WORKDIR /career

# Install required system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    net-tools \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fix: Install spaCy first, then download the model
RUN pip install --no-cache-dir spacy
RUN python -m spacy download en_core_web_sm --direct

# Copy all project files
COPY . .

# Expose required ports
EXPOSE 8501 8502 8503

# Start multiple Streamlit apps
CMD streamlit run app.py --server.port 8501 & \
    streamlit run map.py --server.port 8502 & \
    streamlit run bot.py --server.port 8503 && \
    wait
