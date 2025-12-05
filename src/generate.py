import subprocess
import json

def generate_answer(question, retrieved_chunks):
    # Build clean context
    context = "\n".join([c["meta"]["content"] for c in retrieved_chunks])

    prompt = f"""
You are an intelligent assistant. Answer the following question strictly based on the provided context.
If the answer is present, write it clearly. If the context does not include the answer, say "The answer is not in the document."

Question: {question}

Context:
{context}
"""

    # Run Ollama locally
    result = subprocess.run(
        ["ollama", "run", "llama3.2"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
