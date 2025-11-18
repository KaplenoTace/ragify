"""
3_gradio_frontend.py
Gradio web interface for RAGIFY system
"""

import gradio as gr
import yaml
from src.vector_db import VectorDatabase
from src.embeddings import EmbeddingModel

def load_config():
    """Load configuration from config.yaml"""
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

# Initialize components
config = load_config()
embedding_model = EmbeddingModel(config['embeddings']['model_name'])
vector_db = VectorDatabase(
    collection_name=config['vector_db']['collection_name'],
    persist_directory=config['vector_db']['persist_directory']
)

def query_ragify(query_text, top_k=3):
    """
    Query the RAGIFY system and return results
    
    Args:
        query_text: User's question
        top_k: Number of results to return
    
    Returns:
        Formatted string with results
    """
    if not query_text.strip():
        return "Please enter a query."
    
    # Generate query embedding
    query_embedding = embedding_model.generate_embeddings([query_text])[0]
    
    # Search vector database
    results = vector_db.query(
        query_embedding=query_embedding,
        n_results=top_k
    )
    
    # Format results
    output = f"### 🔍 Top {top_k} Results\n\n"
    
    for idx, (doc, distance) in enumerate(zip(results['documents'][0], results['distances'][0]), 1):
        output += f"**Result {idx}** (Distance: {distance:.4f})\n\n"
        output += f"{doc}\n\n"
        output += "---\n\n"
    
    return output

# Create Gradio interface
with gr.Blocks(title="RAGIFY - RAG Query System", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🤖 RAGIFY - Local RAG System
        
        Ask questions about your documents and get relevant answers powered by vector search!
        """
    )
    
    with gr.Row():
        with gr.Column():
            query_input = gr.Textbox(
                label="Your Question",
                placeholder="e.g., What is machine learning?",
                lines=3
            )
            top_k_slider = gr.Slider(
                minimum=1,
                maximum=10,
                value=3,
                step=1,
                label="Number of Results"
            )
            submit_btn = gr.Button("Search", variant="primary")
        
        with gr.Column():
            output_area = gr.Markdown(label="Results")
    
    # Connect the button to the function
    submit_btn.click(
        fn=query_ragify,
        inputs=[query_input, top_k_slider],
        outputs=output_area
    )
    
    # Add examples
    gr.Examples(
        examples=[
            ["What is machine learning?"],
            ["Explain neural networks"],
            ["How does deep learning work?"]
        ],
        inputs=query_input
    )

if __name__ == "__main__":
    print("🚀 Starting RAGIFY Gradio Interface...")
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)
