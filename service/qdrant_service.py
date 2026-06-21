from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance
)

from setting import settings


class QdrantService:

    def __init__(self):

        self.collection_name = "documents"

        self.client = QdrantClient(
            host=settings.qdrant_host,
            port=settings.qdrant_port
        )

        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self):

        collections = self.client.get_collections()

        collection_names = [
            collection.name
            for collection in collections.collections
        ]

        if self.collection_name not in collection_names:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            )

    def insert_chunk(
        self,
        chunk_id: str,
        vector: list[float],
        payload: dict
    ):

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=chunk_id,
                    vector=vector,
                    payload=payload
                )
            ]
        )

    def search(
        self,
        vector: list[float],
        limit: int = 3
    ):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            limit=limit
        )

        return results.points