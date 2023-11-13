import os
import openai

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

fine_tune_events = openai.FineTune.list_events(id='file-odC56jS9MUtCqcmPp9YWjWRM')