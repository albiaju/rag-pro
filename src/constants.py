import os

EMBEDDING_MODEL_PATH = os.getenv(
    "EMBEDDING_MODEL_PATH", "sentence-transformers/all-mpnet-base-v2"
)
ASSYMETRIC_EMBEDDING = os.getenv("ASSYMETRIC_EMBEDDING", "False").lower() == "true"
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "768"))
TEXT_CHUNK_SIZE = int(os.getenv("TEXT_CHUNK_SIZE", "300"))

OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3.2:1b")
OLLAMA_ADDRESS = os.getenv("OLLAMA_ADDRESS", "http://localhost:11434")
os.environ.setdefault("OLLAMA_ADDRESS", OLLAMA_ADDRESS)

####################################################################################################
# Dont change the following settings
####################################################################################################

# Logging
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "logs/app.log")
# OpenSearch settings
OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST", "localhost")
OPENSEARCH_PORT = int(os.getenv("OPENSEARCH_PORT", "9200"))
OPENSEARCH_INDEX = os.getenv("OPENSEARCH_INDEX", "documents")
