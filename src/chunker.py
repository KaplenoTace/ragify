"""Text Chunking Module - Split documents into manageable chunks"""

from typing import List, Dict
import yaml


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks.
    
    Args:
        text: Input text to chunk
        chunk_size: Size of each chunk in characters
        overlap: Overlap between consecutive chunks
        
    Returns:
        List of text chunks
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        
        if chunk.strip():  # Only add non-empty chunks
            chunks.append(chunk)
        
        start += (chunk_size - overlap)
    
    return chunks


def chunk_documents(documents: List[Dict], chunk_size: int = 300, overlap: int = 50) -> List[Dict]:
    """Chunk multiple documents."""
    all_chunks = []
    
    for doc in documents:
        text_chunks = chunk_text(doc['content'], chunk_size, overlap)
        
        for i, chunk in enumerate(text_chunks):
            all_chunks.append({
                'text': chunk,
                'metadata': {
                    **doc.get('metadata', {}),
                    'chunk_id': i,
                    'total_chunks': len(text_chunks)
                }
            })
    
    return all_chunks


if __name__ == "__main__":
    # Test the chunker
    sample_text = "This is a sample text for testing. " * 50
    chunks = chunk_text(sample_text, chunk_size=100, overlap=20)
    print(f"Created {len(chunks)} chunks")
