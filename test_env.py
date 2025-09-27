import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("✅ API key loaded successfully!")
    print("First 8 characters of your key:", api_key[:8] + "...")
else:
    print("❌ Failed to load API key. Check your .env file.")
