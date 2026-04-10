# ragify

A local RAG (Retrieval-Augmented Generation) system I built to understand how embeddings, chunking, and vector databases actually work together. Runs entirely offline — no API keys, no cloud dependencies.

I made three different ways to interact with it: a Gradio UI, a Streamlit dashboard, and a plain CLI. Started with the CLI for testing, then built the frontends on top.

## What it does

- Loads `.txt` files from a `data/` folder and splits them into chunks with overlap
- Converts those chunks into 384-dimensional vectors using `all-MiniLM-L6-v2`
- Stores everything in a local ChromaDB instance
- At query time, embeds your question and finds the most semantically similar chunks

## Project structure

```
ragify/
├── requirements.txt
├── config.yaml
├── 1_index_documents.py    # step 1: index your docs
├── 2_query_system.py       # step 2: query via CLI
├── 3_gradio_frontend.py    # step 3a: Gradio UI
├── streamlit_app.py        # step 3b: Streamlit dashboard
├── data/
│   └── sample_docs.txt
└── src/
    ├── document_loader.py
    ├── chunker.py
    ├── embeddings.py
    └── vector_db.py
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

**Index your documents first:**
```bash
python 1_index_documents.py
```
This reads everything in `data/`, chunks it, generates embeddings, and saves them to ChromaDB locally.

**Then pick an interface:**

Gradio (simplest):
```bash
python 3_gradio_frontend.py
# http://localhost:7860
```

Streamlit:
```bash
streamlit run streamlit_app.py
# http://localhost:8501
```

CLI:
```bash
python 2_query_system.py
```

## Configuration

Everything lives in `config.yaml`:

```yaml
data_folder: data
chunk_size: 300
chunk_overlap: 50
embedding_model: all-MiniLM-L6-v2
vector_db_path: ./vector_db
top_k: 3
```

Smaller `chunk_size` gives more precise results but more chunks to store. Tweak `top_k` to control how many results come back per query.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `No module named 'gradio'` | `pip install -r requirements.txt` |
| No DB found | Run the indexing script first |
| Port in use | Change the port number in the frontend file |
| Slow first run | Normal — downloading the embedding model (~80MB) once |

## What I learned building this

- How chunking strategy affects retrieval quality (overlap matters a lot)
- ChromaDB's cosine similarity under the hood
- Why sentence-transformers are so good for semantic search
- The difference between retrieval and generation in RAG

## Next steps

- Add PDF support with PyPDF2
- Hook up Ollama for actual answer generation instead of just retrieval
- Try hybrid search (BM25 + semantic)

## License

MIT
