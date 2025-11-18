#!/usr/bin/env python3
"""Index documents and create vector database"""
import yaml
from src.document_loader import load_documents
from src.chunker import chunk_documents
from src.embeddings import EmbeddingModel
from src.vector_db import VectorDatabase

def main():
    print("=== RAGIFY Indexing ===")
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    
    print("\n1. Loading documents...")
    docs = load_documents(config['data_folder'])
    print(f"Loaded {len(docs)} documents")
    
    print("\n2. Chunking...")
    chunks = chunk_documents(docs, config['chunk_size'], config['chunk_overlap'])
    print(f"Created {len(chunks)} chunks")
    
    print("\n3. Generating embeddings...")
    embedder = EmbeddingModel(config['embedding_model'])
    texts = [c['text'] for c in chunks]
    embeddings = embedder.embed_texts(texts)
    
    print("\n4. Storing in vector database...")
    db = VectorDatabase(config['vector_db_path'], config['collection_name'])
    metadatas = [c['metadata'] for c in chunks]
    db.add_documents(texts, embeddings.tolist(), metadatas)
    
    print(f"\n✅ Indexing complete! {db.get_count()} chunks stored.")

if __name__ == "__main__":
    main()
