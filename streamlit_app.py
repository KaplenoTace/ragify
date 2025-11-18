"""
streamlit_app.py
Streamlit web interface for RAGIFY system
"""

import streamlit as st
import yaml
from src.vector_db import VectorDatabase
from src.embeddings import EmbeddingModel

# Page configuration
st.set_page_config(
    page_title="RAGIFY - RAG Query System",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def load_config():
    """Load configuration from config.yaml"""
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

@st.cache_resource
def initialize_components():
    """Initialize embedding model and vector database"""
    config = load_config()
    embedding_model = EmbeddingModel(config['embeddings']['model_name'])
    vector_db = VectorDatabase(
        collection_name=config['vector_db']['collection_name'],
        persist_directory=config['vector_db']['persist_directory']
    )
    return config, embedding_model, vector_db

# Initialize
config, embedding_model, vector_db = initialize_components()

# Header
st.title("🤖 RAGIFY - Local RAG System")
st.markdown("Ask questions about your documents and get relevant answers powered by vector search!")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    top_k = st.slider("Number of Results", min_value=1, max_value=10, value=3)
    
    st.markdown("---")
    st.markdown("""
    ### About RAGIFY
    A complete local Retrieval-Augmented Generation system with:
    - 📄 Document chunking
    - 🧠 Embeddings (Sentence Transformers)
    - 🗄️ Vector database (ChromaDB)
    - 🔍 Semantic search
    """)

# Main content
query = st.text_area(
    "Your Question:",
    placeholder="e.g., What is machine learning?",
    height=100
)

if st.button("🔍 Search", type="primary"):
    if query.strip():
        with st.spinner("Searching..."):
            # Generate query embedding
            query_embedding = embedding_model.generate_embeddings([query])[0]
            
            # Search vector database
            results = vector_db.query(
                query_embedding=query_embedding,
                n_results=top_k
            )
            
            # Display results
            st.markdown("---")
            st.subheader(f"📊 Top {top_k} Results")
            
            for idx, (doc, distance) in enumerate(zip(results['documents'][0], results['distances'][0]), 1):
                with st.expander(f"**Result {idx}** - Distance: {distance:.4f}", expanded=(idx==1)):
                    st.markdown(doc)
    else:
        st.warning("Please enter a question.")

# Example queries
st.markdown("---")
st.markdown("### 💡 Example Queries")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("What is machine learning?"):
        st.session_state.example_query = "What is machine learning?"
        
with col2:
    if st.button("Explain neural networks"):
        st.session_state.example_query = "Explain neural networks"
        
with col3:
    if st.button("How does deep learning work?"):
        st.session_state.example_query = "How does deep learning work?"
