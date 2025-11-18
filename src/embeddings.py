"""Embedding Module"""
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class EmbeddingModel:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        print(f"Loading model: {model_name}...")
        self.model = SentenceTransformer(model_name)
        print("Model loaded!")
    
    def embed_texts(self, texts: List[str]) -> np.ndarray:
        return self.model.encode(texts, show_progress_bar=True)
    
    def embed_single(self, text: str) -> np.ndarray:
        return self.model.encode([text])[0]

if __name__ == "__main__":
    embedder = EmbeddingModel()
    result = embedder.embed_texts(["test"])
    print(f"Shape: {result.shape}")
