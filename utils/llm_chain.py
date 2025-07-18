from transformers import pipeline

def generate_answer(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    qa_pipeline = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=200)
    return qa_pipeline(prompt)[0]['generated_text']
