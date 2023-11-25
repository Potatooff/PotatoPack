import json
import os

class ChatSessionManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.chat_sessions = self.load_chat_sessions()

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

# Example usage
json_file_path = 'chat_sessions.json'  # Replace with your desired file path
chat_manager = ChatSessionManager(json_file_path)

# Adding a chat session
session_name = 'chat_session_1'
file_path = 'path/to/your/chat_session_1.json'
chat_manager.add_chat_session(session_name, file_path)

# Adding another chat session
session_name = 'chat_session_2'
file_path = 'path/to/your/chat_session_2.json'
chat_manager.add_chat_session(session_name, file_path)