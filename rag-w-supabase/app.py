
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pdf_loader import load_documents
from config import openai_api_key

documents = load_documents("./external-data/theanxiousgeneration.pdf")

if documents is None:
    print("No documents loaded. Exiting.")
    exit()

client = OpenAI(api_key=openai_api_key)

while True:
    user_query = input("Enter your query (or type 'exit' to quit): ")

    if user_query.lower() == "exit":
        print("Goodbye!")
        break  # Salimos del loop

    matched_docs = documents.similarity_search(user_query)
    injected_docs = "\n\n".join([doc.page_content for doc in matched_docs])

    completion_messages = [
        {
            "role": "system",
            "content": "You are an AI assistant with unparalleled expertise in mental health and wellness. Your primary goal is to provide accurate and helpful information to users based on their queries. You are capable of understanding and responding to complex queries, providing tailored advice and guidance, and offering valuable insights and recommendations. Your responses should be concise, clear, and informative, and you should strive to provide helpful and accurate information to users. You should also be able to handle a wide range of queries and provide appropriate responses, regardless of the complexity or nuance of the question. Additionally, you should be able to adapt your responses to different user preferences and needs, and you should be able to learn from your interactions with users to improve your responses over time. Overall, your goal is to be a helpful and knowledgeable AI assistant that can assist users in their mental health and wellness journey. If the user asks about other topic, just say that the topic is out of scope for this chatbot.",
        },
        {
            "role": "user",
            "content": user_query,
        },
        {
            "role": "assistant",
            "content": injected_docs,
        },
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=completion_messages,
        max_tokens=400,
        temperature=0.4,
    )
    
    print("\n")
    print("Assistant's Response:")
    print(response.choices[0].message.content)
    print("\n" + "="*50 + "\n")  # Separador para mayor claridad