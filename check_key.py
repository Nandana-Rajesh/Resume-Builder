from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("Key loaded:", key is not None)

if key:
    print("First 8 characters:", key[:8])