"""Vector Database Module"""
import chromadb
from typing import List, Dict

class VectorDatabase:
    def __init__(self, db_path: str = "./vector_db", collection_name: str = "ragify_collection"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name=collection_name)
        print(f"Vector DB ready: {collection_name}")
    
    def add_documents(self, texts: List[str], embeddings: List, metadatas: List[Dict] = None, ids: List[str] = None):
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(texts))]
        self.collection.add(documents=texts, embeddings=embeddings, metadatas=metadatas, ids=ids)
        print(f"Added {len(texts)} documents")
    
    def query(self, query_embedding: List[float], top_k: int = 3) -> Dict:
        results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)
        return results
    
    def get_count(self) -> int:
        return self.collection.count()

if __name__ == "__main__":
    db = VectorDatabase()
    print(f"Database has {db.get_count()} documents")
