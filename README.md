# RAGIFY - Local Retrieval-Augmented Generation System

A complete, beginner-friendly RAG system built entirely locally with **Embeddings**, **Chunking**, **Vector Database**, and **Beautiful Web Frontends** (Gradio & Streamlit).

---

## What's Included

This project covers all RAG fundamentals you learned:
- **Embeddings**: Text → semantic vectors using `sentence-transformers`
- **Chunking**: Smart text splitting with overlap preservation
- **Vector Database**: Local ChromaDB for fast similarity search
- **RAG Pipeline**: Document indexing + intelligent retrieval
- **Web Frontends**: Gradio (simple), Streamlit (professional), CLI
- **Sample Data**: Machine learning documentation included

---

## Project Structure

```
ragify/
├── requirements.txt          # Dependencies (includes Gradio & Streamlit)
├── config.yaml              # All settings in one place
├── README.md                # This guide
├── PROJECT_SUMMARY.txt      # Project overview
│
├── MAIN SCRIPTS
├── 1_index_documents.py     # Step 1: Index your documents
├── 2_query_system.py        # Step 2: CLI query interface
├── 3_gradio_frontend.py     # Step 3a: Gradio web UI (recommended)
├── streamlit_app.py         # Step 3b: Streamlit dashboard
│
├── data/
│   └── sample_docs.txt      # Sample ML documentation
│
└── src/
    ├── __init__.py
    ├── document_loader.py   # Load text documents
    ├── chunker.py          # Split text intelligently
    ├── embeddings.py       # Generate & manage embeddings
    └── vector_db.py        # Vector database operations
```

---

## Quick Start (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Index Your Documents
```bash
python 1_index_documents.py
```
This processes all `.txt` files in the `data/` folder, creates embeddings, and stores them locally.

### 3. Choose Your Interface

**Option A: Gradio (Recommended for Beginners)**
```bash
python 3_gradio_frontend.py
```
Then visit `http://localhost:7860`
- Clean, simple UI
- Adjustable results slider
- Example questions included
- Similarity scores displayed

**Option B: Streamlit (Professional Dashboard)**
```bash
streamlit run streamlit_app.py
```
Then visit `http://localhost:8501`
- Professional dashboard
- Sidebar settings
- Quick example buttons
- Database statistics

**Option C: Command Line (Testing)**
```bash
python 2_query_system.py
```
- Interactive terminal interface
- Great for debugging
- No browser needed

---

## How It Works

### Phase 1: Indexing (Run Once)
```
Documents → Split into Chunks → Generate Embeddings → Store in Vector DB
```

### Phase 2: Querying (Run Anytime)
```
Your Question → Embed It → Find Similar Chunks → Return Results with Scores
```

---

## Understanding Components

### 1. `document_loader.py`
Reads all `.txt` files from the `data/` folder and returns them with metadata.

### 2. `chunker.py`
Splits documents into **300-character chunks** with **50-character overlap** (configurable).

### 3. `embeddings.py`
Uses **all-MiniLM-L6-v2** transformer to convert text into **384-dimensional vectors**.

### 4. `vector_db.py`
Uses **ChromaDB** to store embeddings and find similar chunks via cosine similarity.

### 5. Frontends
- **3_gradio_frontend.py**: Auto-generated beautiful web UI
- **streamlit_app.py**: Customisable professional dashboard
- **2_query_system.py**: CLI for terminal users

---

## Configuration (`config.yaml`)

```yaml
data_folder: data              # Where to find documents
chunk_size: 300               # Characters per chunk
chunk_overlap: 50             # Overlap between chunks
embedding_model: all-MiniLM-L6-v2  # Fast, good model
vector_db_path: ./vector_db   # Where to store database
collection_name: ragify_collection
top_k: 3                      # Number of results per query
```

Adjust these based on your needs:
- Smaller `chunk_size` → more precise but more chunks
- Larger `chunk_size` → faster but less precise
- Higher `top_k` → more results per query

---

## Tips & Tricks

1. **Add More Documents**: Just put `.txt` files in `data/` and re-run indexing
2. **Adjust Results**: Change `top_k` in `config.yaml`
3. **Better Accuracy**: Try different embedding models (BGE, E5)
4. **Test Components**: Each `.py` file in `src/` can run standalone
5. **Performance**: First embedding download takes ~80MB, after that, it's instant

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `No module named 'gradio'` | Run `pip install -r requirements.txt` |
| No database found | Run `python 1_index_documents.py` first |
| Port already in use | Edit port number in frontend file (7860 → 7861) |
| No results found | Check documents are in `data/`, try different questions |
| Slow first run | Normal! Downloading embedding model (~80MB), happens once |

---

## Comparing Frontends

| Feature | CLI | Gradio | Streamlit |
|---------|-----|--------|------------|
| Setup Time | 1 min | 2 min | 3 min |
| Learning Curve | ✓ | ✓✓ | ✓✓✓ |
| UI Quality | None | Good | Excellent |
| **Best For** | Testing | Quick Start | Production |

**Recommendation**: Start with Gradio, then try Streamlit for more features.

---

## Testing Individual Components

```bash
# Test document loader
python src/document_loader.py

# Test chunker
python src/chunker.py

# Test embeddings
python src/embeddings.py

# Test vector database
python src/vector_db.py
```

---

## Next Steps

After mastering the basics:
1. Add PDF support using `PyPDF2`
2. Integrate Ollama for answer generation
3. Deploy to cloud (Hugging Face, Railway, etc.)
4. Add user authentication
5. Implement hybrid search (keyword + semantic)

---

## What You Learned

✓ **Embeddings**: How text becomes vectors with semantic meaning  
✓ **RAG**: How retrieval enhances generation quality  
✓ **Chunking**: How to split documents for optimal search  
✓ **Vector DB**: How to store and search embeddings efficiently  
✓ **Web UI**: How to make AI accessible with simple interfaces

---

## Sample Data

Included `sample_docs.txt` contains:
- Machine Learning fundamentals
- Python for ML
- Deep Learning & Neural Networks
- Natural Language Processing
- Computer Vision
- Data Science workflow
- Evaluation metrics

Perfect for testing and learning!

---

## Key Features

- Works entirely **offline** (no API keys needed)
- Beautiful web interfaces (Gradio & Streamlit)
- Persistent local database
- Fast similarity search
- Configurable chunking & embeddings
- Sample data included
- Well-documented code
- Ready for GitHub

---

## Licence

MIT Licence - Feel free to use, modify, and share!

---

## Contributing

This is a learning project. Feel free to:
- Experiment with different settings
- Try different models
- Add your own features
- Share your improvements

---

## Support

- Check code comments for explanations
- See `FRONTEND_GUIDE.md` for detailed UI usage
- See `PROJECT_SUMMARY.txt` for overview
- Each `.py` file includes docstrings

---

## Ready to Go!

Your RAGIFY system is complete, tested, and ready:
- ✅ All dependencies configured
- ✅ Sample data included
- ✅ Three interface options
- ✅ Full documentation
- ✅ GitHub-ready

**Start with:**
```bash
python 1_index_documents.py
python 3_gradio_frontend.py
```

**Happy Learning!**

---

*Made with ❤️ for data scientists learning RAG systems.*  
*Built entirely locally • No API dependencies • Perfect for beginners*
