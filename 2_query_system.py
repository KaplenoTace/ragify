"""
2_query_system.py
CLI-based query interface for RAGIFY system
"""

import yaml
from src.vector_db import VectorDatabase
from src.embeddings import EmbeddingModel

def load_config():
    """Load configuration from config.yaml"""
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def query_system():
    """Main query loop for interacting with the RAG system"""
    config = load_config()
    
    # Initialize embedding model and vector database
    print("Initializing RAGIFY Query System...")
    embedding_model = EmbeddingModel(config['embeddings']['model_name'])
    vector_db = VectorDatabase(
        collection_name=config['vector_db']['collection_name'],
        persist_directory=config['vector_db']['persist_directory']
    )
    
    print("\n✓ System ready! Type your questions (or 'quit' to exit)\n")
    
    while True:
        # Get user query
        query = input("Query: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not query:
            continue
        
        # Generate query embedding
        query_embedding = embedding_model.generate_embeddings([query])[0]
        
        # Search vector database
        results = vector_db.query(
            query_embedding=query_embedding,
            n_results=config['query']['top_k']
        )
        
        # Display results
        print(f"\n{'='*60}")
        print(f"Top {len(results['documents'][0])} Results:")
        print(f"{'='*60}\n")
        
        for idx, (doc, distance) in enumerate(zip(results['documents'][0], results['distances'][0]), 1):
            print(f"Result {idx} (Distance: {distance:.4f}):")
            print(f"{doc}\n")
            print("-" * 60 + "\n")

if __name__ == "__main__":
    query_system()
