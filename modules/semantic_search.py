from txtai.embeddings import Embeddings

class SemanticSearchEngine:
    def __init__(self):
        # Initialize txtai with an in-memory SQLite backend
        self.embeddings = Embeddings({"path": "sqlite://", "content": True})
        self.embeddings.index([])

    def add_document(self, doc_id, content):
        """
        Adds a document (typically a node's text) to the txtai index.
        """
        self.embeddings.index([(doc_id, content, None)])

    def search(self, query, limit=5):
        """
        Performs a semantic search over the indexed documents.
        """
        return self.embeddings.search(query, limit)
