import json
import os
from src.utils.paths import (
                                data_app_history_chatIds_path
                            )

class ChatSessionManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.chat_sessions = self.load_chat_sessions()

    @staticmethod
    def load_chat_sessions(self):
        try:
            with open(self.json_file_path, 'r') as file:
                chat_sessions = json.load(file)
            return chat_sessions
        except FileNotFoundError:
            return {}

    def save_chat_sessions(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.chat_sessions, file, indent=2)

    def add_chat_session(self, session_name, file_path):
        if session_name not in self.chat_sessions:
            self.chat_sessions[session_name] = {'file_path': []}
        self.chat_sessions[session_name]['file_path'].append(file_path)
        self.save_chat_sessions()

    def delete_chat_session(self, session_name):
        if session_name in self.chat_sessions:
            del self.chat_sessions[session_name]
            self.save_chat_sessions()

class ChatHistoryFile():



    @staticmethod
    def get_query_count(chat_history) -> int:
        return len(chat_history)

    @staticmethod
    def save_chat_history(chat_history, user_id):
        file_path = f'{user_id}_chat_history.json'
        with open(file_path, 'w') as file:
            json.dump(chat_history, file, indent=2)  # Added indent for better readability
        return file_path

    # Function to load chat history from a JSON file
    def load_chat_history(file_path):
        try:
            with open(file_path, 'r') as file:
                chat_history = json.load(file)
            return chat_history
        except FileNotFoundError:
            # If the file doesn't exist yet, return an empty dictionary
            return {}

    # Function to add a message to the chat history
    def add_message(chat_history, query_id, sender, message):
        if query_id not in chat_history:
            chat_history[query_id] = {'user': [], 'assistant': [], 'generated_image': []}
        chat_history[query_id][sender].append(message)

    # Example usage
    user_id = '123'  # Replace with the actual user ID

    # Create a unique chat history file for the user
    user_chat_history_path = save_chat_history({}, user_id)

    # Later, you can load the chat history and update it
    loaded_chat_history = load_chat_history(user_chat_history_path)

    # Add messages to the chat history for query_1
    add_message(loaded_chat_history, 'query_1', 'user', 'Hey, what\'s up?')
    add_message(loaded_chat_history, 'query_1', 'user', 'Thanks for the image!')
    add_message(loaded_chat_history, 'query_1', 'assistant', 'Not much, just chilling. How can I help you today?')
    add_message(loaded_chat_history, 'query_1', 'assistant', 'You\'re welcome! Anything else you need?')


    add_message(loaded_chat_history, 'query_2', 'user', 'Hey, what\'s up?')
    add_message(loaded_chat_history, 'query_2', 'user', 'Thanks for the image!')
    add_message(loaded_chat_history, 'query_2', 'assistant', 'Not much, just chilling. How can I help you today?')
    add_message(loaded_chat_history, 'query_2', 'assistant', 'You\'re welcome! Anything else you need?')

    # Save the updated chat history
    save_chat_history(loaded_chat_history, user_id)





    query_count = get_query_count(loaded_chat_history)

    # Print the result
    print(f'The number of queries is: {query_count}')