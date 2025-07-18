

#  Mini RAG QA System 

##  Objective

This project implements a **Retrieval-Augmented Generation (RAG)** based Question-Answering (QA) system using an open-source LLM. The system enables users to upload a medical document (PDF/DOCX/TXT), ask domain-related questions, and receive generated answers grounded in the uploaded content.

---

## 🛠️ Tools and Models Used

| Category         | Tool/Model                                     | Purpose                                          |
| ---------------- | ---------------------------------------------- | ------------------------------------------------ |
| **Programming**  | Python                                         | Core development language                        |
| **Frontend**     | Streamlit                                      | UI for file upload, question input, output       |
| **LLM**          | `tiiuae/falcon-rw-1b` (via HuggingFace)        | Answer generation from context                   |
| **Embeddings**   | `all-MiniLM-L6-v2` (Sentence Transformers)     | Text chunk embedding                             |
| **Vector Store** | FAISS                                          | Efficient semantic search                        |
| **Libraries**    | `LangChain`, `transformers`, `huggingface_hub` | Document loading, embedding, and LLM integration
| **File Support** | .pdf, .txt, .docx                              |


---

##  Design Decisions and Assumptions

1. **Chunking Strategy:**

   * Used `RecursiveCharacterTextSplitter` with `chunk_size=500` and `overlap=100`.
   * Balances retrieval quality and performance.

2. **LLM Selection:**

   * Chose `tiiuae/falcon-rw-1b` due to local availability via HuggingFace hub and manageable size.
   * Ensures free-tier accessibility, as required.

3. **File Handling:**

   * Supports `.pdf`, `.docx`, and `.txt` uploads.
   * Converts uploaded files into text before embedding.

4. **Interface:**

   * Built with Streamlit for interactive usage.
   * Provides:

     * File upload
     * Manual query input
     * Sample test case execution
     * Answer download buttons

5. **Data Storage:**

   * FAISS used to store vectorized chunks.
   * Embeddings stored locally for fast retrieval.

---

## Where AI Tools (ChatGPT/Copilot) Were Used

ChatGPT was used as a coding assistant for:

Understanding and verifying RAG architecture.

Writing initial boilerplate code for document loaders and chunking.

Debugging LangChain deprecation warnings.

---

##  Limitations (Due to Time/Resource Constraints)

1. **LLM Performance:**

   * Falcon-RW-1B is a small-scale model; while lightweight, it may not generate expert-level medical responses consistently.
   * Larger models (e.g., Mistral-7B, LLaMA2) were avoided due to hardware/memory limits.

2. **Caching:**

   * Vectorstore and answer caching not implemented to reduce setup time.

3. **Re-ranking:**

   * Maximal Marginal Relevance (MMR) or other reranking algorithms were not included.

4. **Local CPU Mode:**

   * Model runs on CPU, which affects performance and generation speed.

5. **Testing Scope:**

   * Only sample questions provided in the assessment were tested (`Recurrent depressive disorder...`, `OCD criteria...`).

---

##  Sample Output

**Sample Question:**
`Give me the correct coded classification for the following diagnosis: Recurrent depressive disorder, currently in remission`

**Answer:**
*(Generated answer appears  can also be downloaded as a .txt file.)*

---
## Completed Requirements Summary
| Requirement                            
| -------------------------------------- 
| Document ingestion and chunking        
| Embedding and vector store setup       
| Query input and semantic retrieval     
| LLM answer generation                  
| Sample test question support           
| Streamlit UI with file upload/download 
| Multiple file format support           
| Output styling and download           


##  Project Structure

```
mini-rag-qa/
│
├── main.py                        # Streamlit frontend
├── utils/
│   ├── ingest.py                  # Document loading and chunking
│   ├── embed_store.py             # Embedding and FAISS vector store
│   └── llm_chain.py               # LLM-based answer generation
├── data/                          # Stores uploaded files and vectorstore
├── README.md                      # Explanatory note
```


