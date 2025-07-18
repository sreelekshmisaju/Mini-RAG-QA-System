import streamlit as st
from utils.ingest import load_and_chunk, load_docx_or_txt  # Make sure this is implemented
from utils.embed_store import embed_and_store, retrieve_relevant_chunks
from utils.llm_chain import generate_answer
import os

# Set Streamlit app configuration
st.set_page_config(page_title="Mini RAG QA System", layout="centered")
st.title("🧠 Mini RAG QA System")

# Upload block
uploaded_file = st.file_uploader("📄 Upload a  file (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
query = st.text_input("❓ Ask your question here:")
generate_btn = st.button("🔍 Generate Answer")

# Pipeline Setup (Embedding + Chunking)
@st.cache_resource
def setup_pipeline(file_path, file_type):
    if file_type == "pdf":
        chunks = load_and_chunk(file_path)
    else:
        chunks = load_docx_or_txt(file_path)
    embed_and_store(chunks)
    return True

# If file is uploaded
if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    file_path = f"data/input.{file_extension}"
    os.makedirs("data", exist_ok=True)

    # Save the uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Run pipeline
    setup_pipeline(file_path, file_extension)

    # On generate button click
    if query and generate_btn:
        docs = retrieve_relevant_chunks(query)
        context = "\n".join([doc.page_content for doc in docs])
        answer = generate_answer(query, context)

        st.subheader("💬 Answer")
        st.markdown(
            f"""
            <div style='background-color:#ffffff; color:#000000;
                        padding:15px; border-radius:10px;
                        border:1px solid #d1d1d1; font-size:16px'>
                <strong>Answer:</strong><br>{answer}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.download_button(
            label="📥 Download Answer",
            data=answer,
            file_name="generated_answer.txt",
            mime="text/plain"
        )

# Horizontal separator
st.markdown("---")

# Sample Test Case button
if st.button("▶ Run Sample Test Case"):
    sample_question = "Give me the correct coded classification for the following diagnosis: Recurrent depressive disorder, currently in remission"
    docs = retrieve_relevant_chunks(sample_question)
    context = "\n".join([doc.page_content for doc in docs])
    answer = generate_answer(sample_question, context)

    st.subheader("🧪 Sample Test Case")
    st.markdown(f"**Question:** {sample_question}")
    st.markdown(
        f"""
        <div style='background-color:#ffffff; color:#000000;
                    padding:15px; border-radius:10px;
                    border:1px dashed #aaa; font-size:16px'>
            <strong>Answer:</strong><br>{answer}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.download_button(
        label="📥 Download Sample Answer",
        data=answer,
        file_name="sample_answer.txt",
        mime="text/plain"
    )
