## Description
This is an application that allows users to interact with a text, pdf or word document using conversational AI techniques. The chatbot leverages the OpenAI GPT-3.5 model and Pinecone vectore store to deliver responses to user inquiries, utilizing the content of the loaded document.

## Features
- Loads a text, pdf or word document. 
- Preprocesses the document for better compatibility with the chatbot model
- Builds a conversation chain using the preprocessed document
- Allows users to ask questions and receive answers from the chatbot
- Provides a chat history for tracking previous interactions

## Limitations
- The accuracy and relevance of the chatbot's answers depend on the quality and comprehensiveness of the loaded document.

## Installation
- Clone the repository: `git clone https://github.com/KevKibe/Document-Chatbot/.git`
- Install dependencies: `pip install -r requirements.txt`
- Set up environment variables: Create a `.env` file in the root directory of the project and add your OpenAI API key as follows:
  `OPENAI_API_KEY=your_api_key_here` , `PINECONE_API_KEY="your_api_key"` , `PINECONE_ENVIRONMENT="your_environment"` ,  `PINECONE_INDEX_NAME="index_name"`

## Usage
- Run the application: `python main.py`
- Enter the file directory.
- Enter your queries in the console prompt and press Enter.
- The chatbot will process your query and provide an answer based on the content of the file.
- Continue the conversation by entering additional queries.
- Exit the conversatio by entering command `q`


**:zap: I'm currently open for roles in Data Science, Machine Learning, NLP and Computer Vision.**
