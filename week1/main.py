import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Step 3: Check whether the API key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in .env")

# Step 4: Create the Gemini client
client = genai.Client(api_key=api_key)

# Step 5: Send a prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Step 6: Display the response
print("\nGemini Response:")
print(response.text)