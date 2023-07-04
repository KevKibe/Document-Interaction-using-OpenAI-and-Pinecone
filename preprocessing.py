from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import pinecone
import configparser

config = configparser.ConfigParser()
config.read('.env')
openai_key = config.get('openai', 'OPENAI_API_KEY')
pinecone_env_key = config.get('pinecone', 'PINECONE_ENVIRONMENT')
pinecone_api_key = config.get('pinecone', 'PINECONE_API_KEY')

class Preprocessor:
    def get_text_chunks(self, text):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_documents(text)
        return chunks

    def get_vectorstore(self, text_chunks):
        config = configparser.ConfigParser()
        config.read('.env')
        pinecone_api_key = config.get('pinecone', 'PINECONE_API_KEY')
        index_name = config.get('pinecone', 'PINECONE_INDEX_NAME')
    
        pinecone.init(api_key=pinecone_api_key)
        pinecone.create_index(index_name=index_name, metric="cosine")
        index = pinecone.Index(index_name=index_name)
        index.upsert(items={i: text_chunks[i] for i in range(len(text_chunks))})
        return index


class ConversationChain:
    def get_conversation_chain(self, vectorstore):
        llm = ChatOpenAI()

        memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain
