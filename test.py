import json

class ChatHistory:
    def __init__(self):
        self.chat_history = {}
        self.load_from_file()

    def add_chat(self, chat_name):
        if chat_name not in self.chat_history:
            self.chat_history[chat_name] = {}
            print(f"Chat {chat_name} added successfully!")
            self.save_to_file()
        else:
            print(f"Chat {chat_name} already exists. Choose a different name.")

    def add_user_query(self, chat_name, user_query):
        if chat_name in self.chat_history:
            self.chat_history[chat_name]["user_query"] = user_query
            print(f"User query added to {chat_name} successfully!")
            self.save_to_file()
        else:
            print(f"Chat {chat_name} not found.")

    def add_chatbot_response(self, chat_name, chatbot_response):
        if chat_name in self.chat_history:
            self.chat_history[chat_name]["chatbot_response"] = chatbot_response
            print(f"Chatbot response added to {chat_name} successfully!")
            self.save_to_file()
        else:
            print(f"Chat {chat_name} not found.")

    def delete_chat(self, chat_name):
        if chat_name in self.chat_history:
            del self.chat_history[chat_name]
            print(f"Chat {chat_name} deleted successfully!")
            self.save_to_file()
        else:
            print(f"Chat {chat_name} not found.")

    def delete_user_query(self, chat_name):
        if chat_name in self.chat_history:
            del self.chat_history[chat_name]["user_query"]
            print(f"User query for {chat_name} deleted successfully!")
            self.save_to_file()
        else:
            print(f"Chat {chat_name} not found.")

    def delete_chat_response(self, chat_name):
        if chat_name in self.chat_history:
            del self.chat_history[chat_name]["chatbot_response"]
            self.save_to_file()
            print(f"Chat response for {chat_name} deleted successfully!")

        else:
            print(f"Chat {chat_name} not found.")

    def save_to_file(self, filename='chat_history.json'):
        with open(filename, 'w') as file:
            json.dump(self.chat_history, file, indent=2)
        print("Chat history saved successfully!")

    def get_all_chats(self):
        return list(self.chat_history.keys())

    def get_user_query(self, chat_name):
        if chat_name in self.chat_history:
            return self.chat_history[chat_name].get("user_query", "User query not available for this chat.")
        else:
            return f"Chat {chat_name} not found."

    def get_chatbot_response(self, chat_name):
        if chat_name in self.chat_history:
            return self.chat_history[chat_name].get("chatbot_response", "Chatbot response not available for this chat.")
        else:
            return f"Chat {chat_name} not found."
        

    def load_from_file(self, filename='chat_history.json'):
        try:
            with open(filename, 'r') as file:
                self.chat_history = json.load(file)
            print("Chat history loaded successfully!")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty chat history.")

# Example usage:
chat_history_manager = ChatHistory()
# Adding a chat
#chat_history_manager.add_chat("chat_1")

# Adding user query
#chat_history_manager.add_user_query("chat_1", "Make an image of a cute cat")

# Adding chatbot response
#chat_history_manager.add_chatbot_response("chat_1", ["Generating image of a cute cat", "path_to_image.png"])

# Getting all chats
all_chats = chat_history_manager.get_all_chats()
print("All Chats:", all_chats)

# Getting user query for a specific chat
user_query = chat_history_manager.get_user_query("chat_1")
print("User Query:", user_query)

# Getting chatbot response for a specific chat
chatbot_response = chat_history_manager.get_chatbot_response("chat_1")
print("Chatbot Response:", chatbot_response)
