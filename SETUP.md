# RAGIFY Setup Guide

Complete installation and setup instructions for RAGIFY.

---

## Prerequisites

- **Python**: 3.8 or higher
- **pip**: Latest version recommended
- **Git**: For cloning the repository
- **Operating System**: Windows, macOS, or Linux

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/KaplenoTace/ragify.git
cd ragify
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `sentence-transformers` - For embeddings
- `chromadb` - Vector database
- `gradio` - Web interface framework
- `streamlit` - Alternative web interface
- `pyyaml` - Configuration management

### 4. Verify Installation

```bash
python -c "import chromadb; import sentence_transformers; import gradio; import streamlit; print('All dependencies installed successfully!')"
```

---

## Configuration

### Edit `config.yaml`

The default configuration should work out of the box, but you can customize:

```yaml
embeddings:
  model_name: "sentence-transformers/all-MiniLM-L6-v2"  # Change embedding model
  
chunking:
  chunk_size: 500      # Adjust chunk size for your documents
  overlap: 50          # Adjust overlap between chunks
  
vector_db:
  collection_name: "ragify_collection"
  persist_directory: "./chroma_db"
  
query:
  top_k: 3             # Number of results to return
```

---

## Usage

### Step 1: Index Your Documents

Place your documents in the `data/` folder, then run:

```bash
python 1_index_documents.py
```

**Expected Output:**
```
Loading documents from data/...
Found 1 documents
Chunking documents...
Created 15 chunks
Generating embeddings...
Storing in vector database...
✓ Indexing complete! 15 chunks stored.
```

### Step 2: Query the System

#### Option A: CLI Interface

```bash
python 2_query_system.py
```

**Example:**
```
Initializing RAGIFY Query System...
✓ System ready! Type your questions (or 'quit' to exit)

Query: What is machine learning?
```

#### Option B: Gradio Web Interface

```bash
python 3_gradio_frontend.py
```

Then open: `http://localhost:7860`

#### Option C: Streamlit Web Interface

```bash
streamlit run streamlit_app.py
```

Then open: `http://localhost:8501`

---

## Adding Your Own Documents

### Supported Formats
- `.txt` files (currently)
- Add your documents to the `data/` folder
- Re-run `python 1_index_documents.py` to index new documents

### Example Document Structure

```
data/
├── company_handbook.txt
├── technical_docs.txt
└── faq.txt
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError`
**Solution:** Ensure you've activated your virtual environment and installed dependencies:
```bash
pip install -r requirements.txt
```

### Issue: ChromaDB Persistence Error
**Solution:** Delete the `chroma_db/` folder and re-run indexing:
```bash
rm -rf chroma_db
python 1_index_documents.py
```

### Issue: Out of Memory
**Solution:** Reduce `chunk_size` in `config.yaml` or process fewer documents at once.

### Issue: Slow Embedding Generation
**Solution:** The default model runs on CPU. For faster performance:
- Use a smaller model in `config.yaml`
- Reduce the number of documents
- Use GPU if available (PyTorch with CUDA)

---

## Advanced Configuration

### Using a Different Embedding Model

Edit `config.yaml`:
```yaml
embeddings:
  model_name: "sentence-transformers/paraphrase-MiniLM-L6-v2"
```

Available models: https://www.sbert.net/docs/pretrained_models.html

### Adjusting Chunk Size

Larger chunks = more context, but less precise retrieval:
```yaml
chunking:
  chunk_size: 1000
  overlap: 100
```

### Changing Database Location

```yaml
vector_db:
  persist_directory: "/path/to/your/database"
```

---

## Next Steps

1. ✅ Index your documents
2. ✅ Query via CLI or web interface
3. 🔄 Experiment with different embedding models
4. 🔄 Adjust chunk sizes for your use case
5. 🚀 Deploy with Docker (see deployment docs)

---

## Need Help?

- Check the main `README.md` for feature overview
- Review `PROJECT_SUMMARY.txt` for architecture details
- Open an issue on GitHub for bugs or questions

Happy querying! 🚀
