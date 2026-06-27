import os
from dotenv import load_dotenv
import google.generativeai as genai

#print("Running test_gemini.py")
#print("Model = Gemini 2.5 Flash")
load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("API Key:", key)
print("Length:", len(key))

genai.configure(api_key=key)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Hi")

print(response.text)