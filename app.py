import streamlit as st
from PyPDF2 import PdfReader
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS 
from docx2pdf import convert
import os
import openai
import sys

openai_api_key = st.secrets["openai"]["api_key"]

#input file loader
def load_file(file_path):
    documents = []

    if file_path is not None:
        file_name = file_path.name
        if file_name.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())
        elif file_name.endswith('.docx') or file_name.endswith('.doc'):
            loader = Docx2txtLoader(file_path)
            documents.extend(loader.load())
        elif file_name.endswith('.txt'):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

    return documents


 #splitting into chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_documents(text)
    return chunks 
  
 #text embedding
def get_vectorstore(text_chunks):
    vectordb = Chroma.from_documents(text_chunks, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key)
                                     )
    return vectordb

#conversationchain
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def run_convo():
    st.write('Get Information from Law Docs Using Natural Language')
    st.title("Document Upload")
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "doc", "txt"])
    
   # if uploaded_file is not None:
    docs = load_file(uploaded_file)
        
    chunks = get_text_chunks(docs)
    vectordb= get_vectorstore(chunks)



    
    pdf_qa = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(openai_api_key=openai_api_key,temperature=0.7, model_name='gpt-3.5-turbo'),
        retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
        return_source_documents=True,
        verbose=False
    )

    chat_history = []
    query = st.text_input("Prompt: ")
    if query:
        result = pdf_qa({"question": query, "chat_history": chat_history})
        st.write("Answer: " + result["answer"])
        chat_history.append((query, result["answer"]))

run_convo()



  
  
  
  
