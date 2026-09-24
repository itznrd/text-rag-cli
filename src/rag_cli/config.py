from dotenv import load_dotenv
import os
from groq import Groq

# load env and Initialize groq client

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("Groq API key is missing")

groq_client = Groq(api_key=groq_api_key)

MODEL_NAME = "openai/gpt-oss-120b"

