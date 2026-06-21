from fastapi import UploadFile
import uuid

class DocumentService:

    def __init__(
        self,
        pdf_service,
        chunk_service,
        embedding_service,
        qdrant_service
    ):
        self.pdf_service = pdf_service
        self.chunk_service = chunk_service
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def ingest(
        self,
        name: str,
        file: UploadFile
    ):

        file_path = f"documents/{file.filename}"

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        text = self.pdf_service.load_text(
            file_path
        )

        chunks = self.chunk_service.chunk_text(
            text
        )

        for chunk in chunks:

            vector = self.embedding_service.generate_embedding(
                chunk
            )

            payload = {
                "file_name": file.filename,
                "chunk_text": chunk
            }

            self.qdrant_service.insert_chunk(
                chunk_id=str(uuid.uuid4()),
                vector=vector,
                payload=payload
            )

        return {
            "message": "Document uploaded successfully"
        }