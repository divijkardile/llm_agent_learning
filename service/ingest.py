from service.pdf_service import PdfService
from service.chunk_service import ChunkService
from service.embedding_service import EmbeddingService
from service.qdrant_service import QdrantService


pdf_service = PdfService()
chunk_service = ChunkService()
embedding_service = EmbeddingService()
qdrant_service = QdrantService()


text = pdf_service.load_text(
    "documents/employee_handbook.pdf"
)

chunks = chunk_service.chunk_text(text)

for index, chunk in enumerate(chunks):

    vector = embedding_service.generate_embedding(
        chunk
    )

    qdrant_service.insert_chunk(
        chunk_id=index,
        text=chunk,
        vector=vector
    )

print("Ingestion completed")