from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def test_api_key():
    try:
        client = OpenAI()
        # Try a simple completion to test the API key
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API key is working!'"}]
        )
        print("Success! API Response:", response.choices[0].message.content)
        return True
    except Exception as e:
        print("Error testing API key:", str(e))
        return False

if __name__ == "__main__":
    test_api_key()
