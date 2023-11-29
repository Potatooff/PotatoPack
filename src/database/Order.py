import json
from src.utils.paths import data_app_history_order_path

class ChatSessionManager:
    def __init__(self):
        self.chat_sessions = self.load_chat_sessions()

    def load_chat_sessions(self):
        try:
            with open(data_app_history_order_path, 'r') as file:
                chat_sessions = json.load(file)
            return chat_sessions
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        

    def save_chat_sessions(self):
        with open(data_app_history_order_path, 'w') as file:
            json.dump(self.chat_sessions, file, indent=2)


    def add_chat_session(self, file_path):
        session_name: str = "chat_session_" + str(len(self.chat_sessions) + 1)
        if session_name not in self.chat_sessions:
            self.chat_sessions[session_name] = {'file_path': []}
        self.chat_sessions[session_name]['file_path'].insert(0, file_path)
        self.save_chat_sessions()

        return session_name


    def delete_chat_session(self, session_name):
        if session_name in self.chat_sessions:
            del self.chat_sessions[session_name]
            self.save_chat_sessions()

    def get_file_paths(self, session_name):
        if session_name in self.chat_sessions:
            return self.chat_sessions[session_name].get('file_path', [])
        else:
            return []
        
    def get_all_sessions(self):
        return list(self.chat_sessions.keys())
    
    def format_all_sessions(self):
        return [i.replace('chat_', '') for i in self.get_all_sessions()]

# Example usage
#chat_manager = ChatSessionManager()

# Adding a chat session
#file_path = 'path/to/your/chat_session_1.json'
#chat_manager.add_chat_session( file_path)


#print(chat_manager.get_file_paths('chat_session_1')[0])
