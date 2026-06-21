from service.bot import Bot
from service.embedding_service import EmbeddingService
from service.qdrant_service import QdrantService
from service.document_service import DocumentService
from service.pdf_service import PdfService
from service.chunk_service import ChunkService

def get_bot_service():
    embedding_service = EmbeddingService()
    qdrant_service = QdrantService()
    return Bot(embedding_service, qdrant_service)

def get_document_service():

    return DocumentService(
        PdfService(),
        ChunkService(),
        EmbeddingService(),
        QdrantService()
    )