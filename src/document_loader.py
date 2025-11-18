"""Document Loader Module - Load text documents from data folder"""

import os
from pathlib import Path
from typing import List, Dict


def load_documents(data_folder: str = "data") -> List[Dict[str, str]]:
    """Load all .txt files from the specified folder.
    
    Args:
        data_folder: Path to folder containing documents
        
    Returns:
        List of dictionaries with 'content' and 'metadata'
    """
    documents = []
    data_path = Path(data_folder)
    
    if not data_path.exists():
        print(f"Warning: {data_folder} does not exist")
        return documents
    
    for file_path in data_path.glob("*.txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                documents.append({
                    "content": content,
                    "metadata": {
                        "filename": file_path.name,
                        "path": str(file_path)
                    }
                })
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    
    return documents


if __name__ == "__main__":
    # Test the loader
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")
    for doc in docs:
        print(f"- {doc['metadata']['filename']}: {len(doc['content'])} characters")
