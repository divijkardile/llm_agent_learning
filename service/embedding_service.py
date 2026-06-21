import ollama


class EmbeddingService:

    def generate_embedding(
        self,
        text: str
    ) -> list[float]:

        response = ollama.embed(
            model="nomic-embed-text",
            input=text
        )

        return response["embeddings"][0]