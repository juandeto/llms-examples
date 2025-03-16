import os
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from db import supabase
from langchain_core.documents import Document


import hashlib

def hash_text(text: str) -> str:
    """Generate a SHA-256 hash of the text to uniquely identify documents."""
    return hashlib.sha256(text.encode()).hexdigest()

def sanitize_text(text: str) -> str:
    return text.replace("\u0000", "")

def load_documents(path: str) -> list[dict]:
    title = path.split("/")[-1]

    existing_doc_query = supabase.table("documents") \
    .select("*") \
    .eq("metadata->>source", title) \
    .execute()

    print(f"Checking if document '{title}' exists in the database...")
    print(existing_doc_query.data)

    embeddings = OpenAIEmbeddings()

    if existing_doc_query.data:
        print(f"Document '{path}' already exists in the database. Skipping processing.")
        vector_store = SupabaseVectorStore.from_documents(embeddings, client=supabase, table_name="documents", query_name="match_documents")
        return vector_store
        
    loader = PyPDFLoader(path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    split_docs = text_splitter.split_documents(documents)

    # Convert to LangChain Document objects
    new_docs = [
        Document(page_content=sanitize_text(doc.page_content), metadata={"source": title})
        for doc in split_docs
    ]

    # Insert new documents into Supabase
    vector_store = SupabaseVectorStore.from_documents(new_docs, embeddings, client=supabase, table_name="documents", query_name="match_documents")

    print(f"Inserted {len(new_docs)} new documents from '{path}'.")
    return vector_store