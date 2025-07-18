
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def embed_and_store(docs):
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedder)
    vectorstore.save_local("vector_store/")
    return vectorstore

def load_vector_store():
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local("vector_store/", embedder, allow_dangerous_deserialization=True)


def retrieve_relevant_chunks(query, k=3):
    vs = load_vector_store()
    return vs.similarity_search(query, k=k)
