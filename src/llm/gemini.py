import google.generativeai as genai
from src.ui.config import Config


def initialize_gemini():
    """
    Initializes and returns the Gemini LLM model using
    API key and model name from the configuration.
    """
    config = Config()
    api_key = config.get_gemini_api_key()
    model_name = config.get_gemini_model()

    if not api_key:
        raise ValueError(" Gemini API key not found ")

    genai.configure(api_key=api_key)
    llm = genai.GenerativeModel(model_name)

    return llm




















# class GeminiLLM:
#     def __init__(self):
#         self.config = Config()
#         self.api_key = os.getenv("GEMINI_API_KEY")
#         self.model_name = self.config.get_gemini_model()
#         self.llm = None    
          
#     def initialize_gemini(self):
#         if not self.api_key:
#             raise ValueError("Gemini API key not found in config.ini") 

#         genai.configure(api_key=self.api_key)
#         llm = genai.GenerativeModel(self.model_name)
#         return llm
 
















