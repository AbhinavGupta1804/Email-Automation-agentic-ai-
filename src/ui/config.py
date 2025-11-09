import configparser
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    def __init__(self, file_path="./src/ui/config.ini"):
        self.config = configparser.ConfigParser()

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found!")

        self.config.read(file_path)

    def get_gemini_model(self):
        return self.config.get("GEMINI", "MODEL")
    
    def get_gemini_api_key(self):
        return os.getenv("GEMINI_API_KEY")

    def get_sender_email(self):
        return os.getenv("SENDER_EMAIL")
    
    def get_sendgrid_api_key(self):
        return os.getenv("SENDGRID_API_KEY") 



