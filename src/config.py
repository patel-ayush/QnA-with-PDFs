import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_API_MODEL = "gpt-4o-mini"

OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")


