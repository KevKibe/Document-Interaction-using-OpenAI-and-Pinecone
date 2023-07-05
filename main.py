import sys
import time
from file_loader import DocumentLoader
from preprocessing import Chunks, Vectorstore, ConversationChain


class DocumentChatApp:
    def __init__(self):
        start_time = time.time()
        self.document_loader = DocumentLoader()
        self.chunks = Chunks()
        self.preprocessor = Vectorstore()
        self.conversation_chain = ConversationChain()
        self.chat_history = []
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.2f} seconds")
    def run(self):
        yellow = "\033[0;33m"
        green = "\033[0;32m"
        white = "\033[0;39m"
        
        print(f"{yellow}---------------------------------------------------------------------------------")
        print('Natural Language Based Document Quering')
        print('---------------------------------------------------------------------------------')
        
        
        file_directory = input(f"{green}Enter the directory of the document: ")
        
        documents = self.document_loader.load_file(file_directory)
        #start_time = time.time()  

        if not documents:
            print(f"{white}No documents found in the specified directory.")
            return
        
        print(f"{white}Documents loaded successfully.")

        #end_time = time.time()  
        
             

        while True:
            query = input(f"{green}Prompt: ")
            
            if query == "exit" or query == "quit" or query == "q" or query == "f":
                print('\033[32m' + 'Exiting')
                sys.exit()
                
            if query == '':
                continue
                
            result = self.conversation_chain.get_conversation_chain({"question": query, "chat_history": self.chat_history})
            print(f"{white}Answer: " + result["answer"])
            self.chat_history.append((query, result["answer"]))

if __name__ == "__main__":
    app = DocumentChatApp()
    app.run()
