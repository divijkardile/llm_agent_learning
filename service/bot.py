from ollama import chat

class Bot:

    def __init__(self, embedding_service, qdrant_service):
        self.embedding_service = embedding_service
        self.qdrant_service = qdrant_service

    def ask(self, question: str):
        # Generate embedding for the user's prompt
        prompt_vector = self.embedding_service.generate_embedding(question)

        # Search for similar chunks in Qdrant
        similar_chunks = self.qdrant_service.search(prompt_vector)

        # Construct context from similar chunks
        context = "\n".join([chunk.payload["chunk_text"] for chunk in similar_chunks])

        prompt = f"""
        Answer ONLY from the provided context.

        If the answer is not present in the context,
        respond with:

        "I couldn't find this information in the uploaded documents."

        Context:
        {context}

        Question:
        {question}
        """

        # Ask the LLM with the context
        response = chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Context: {prompt}"}
            ]
        )
        return response.message.content