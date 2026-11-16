# main.py

import os
from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient
from mongo_logger import MongoLogger


def main():

    load_dotenv()

    print("===== LLM Monitoring System =====")

    print("1. Gemini")
    print("2. Ollama")

    choice = input("Choose your provider (1/2): ")

    if choice == "1":

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            print("Gemini API key not found in .env file!")
            return

        provider = GeminiProvider(api_key)

    elif choice == "2":

        provider = OllamaProvider()

    else:

        print("Invalid choice!")
        return

    logger = MongoLogger()

    try:

        client = LLMClient(provider, logger)

        prompt = input("\nEnter your prompt: ")

        print("\nGenerating response...\n")

        response = client.generate(prompt)

        print("===== AI Response =====")
        print(response)

    except Exception as error:

        print("Error:", error)

    finally:

        logger.close()


if __name__ == "__main__":
    main()