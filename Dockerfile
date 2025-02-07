FROM python:3.12-slim

WORKDIR /career

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY . .

EXPOSE 8501 8502 8503

CMD streamlit run app.py --server.port 8501 & \
    streamlit run map.py --server.port 8502 & \
    streamlit run bot.py --server.port 8503 && \
    wait

