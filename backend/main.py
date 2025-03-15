from fastapi import FastAPI #type: ignore

from app.schema import(
    ChatRequest
)

from app.db import *
from app.libs import *

import faiss #type:ignore
import numpy as np
from sentence_transformers import SentenceTransformer #type:ignore

app = FastAPI()

cache =InMemoryCache()
set_llm_cache(cache)

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embedding_dim = 384 
faiss_index = faiss.IndexFlatL2(embedding_dim)
faiss_cache = {}


template = PromptTemplate.from_template(
"""
{context}

Trả lời các câu hỏi sau:
{question}

{context_db}
Trả lời ở đây:

"""
)

llm= OllamaLLM(
    base_url="http://localhost:11434",
    model="gemma3:1b"
)

llm_chain =(
    template 
    | llm
    | StrOutputParser()   
)

db = SQLDatabase(engine)

@app.on_event("startup")
def connect_db():
    create_tables()

@app.post("/callback")
def prompt(chat_request: ChatRequest, session_db: SessionDeps):
    prompt_text= chat_request.prompt.strip()
    query_embedding = embedding_model.encode([prompt_text]).astype(np.float32)  
    query_embedding = query_embedding.reshape(1, -1)
    if faiss_index.ntotal > 0: 
        D, I = faiss_index.search(query_embedding, 1)  

        if D[0][0] < 0.8:  
            print("🟢 Semantic Cache Hit - Using FAISS cached response")
            return {"result": faiss_cache[I[0][0]]}  

    print("🔴 Cache Miss - Generating new response")

    context_db = f"Câu trả lời tham khảo từ dữ liệu sẵn có:\n{db.get_table_info(db.get_usable_table_names())}"

    result = llm_chain.invoke({
        "context": chat_request.context,
        "context_db": context_db,
        "question": prompt_text
    })

    index_id = faiss_index.ntotal  
    faiss_index.add(query_embedding)  
    faiss_cache[index_id] = result 

    new_entry = DataChat(prompt=prompt_text, result=result)
    session_db.add(new_entry)
    session_db.commit()

    return {"result": result}