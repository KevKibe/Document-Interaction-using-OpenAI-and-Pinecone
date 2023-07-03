import configparser






config = configparser.ConfigParser()
config.read('.env')
openai_key = config.get('openai', 'OPENAI_API_KEY')
pinecone_env_key = config.get('pinecone', 'PINECONE_ENVIRONMENT')
pinecone_api_key = config.get('pinecone', 'PINECONE_API_KEY')


class DocumentChatApp:
    def __init__(self):
        self.document_loader = DocumentLoader()
        self.preprocessor = Preprocessor()
        self.conversation_chain = ConversationChain()
        self.chat_history = []
        openai.api_key = openai_api_key

    def run(self):
        yellow = "\033[0;33m"
        green = "\033[0;32m"
        white = "\033[0;39m"
        
        print(f"{yellow}---------------------------------------------------------------------------------")
        print('Start your chat-based interaction with your documents')
        print('---------------------------------------------------------------------------------')
        
        while True:
            query = input(f"{green}Prompt: ")
            
            if query == "exit" or query == "quit" or query == "q" or query == "f":
                print('\033[32m' + 'Exiting')
                sys.exit()
                
            if query == '':
                continue
                
            result = self.conversation_chain({"question": query, "chat_history": self.chat_history})
            print(f"{white}Answer: " + result["answer"])
            self.chat_history.append((query, result["answer"]))

if __name__ == "__main__":
    app = DocumentChatApp()
    app.run()
