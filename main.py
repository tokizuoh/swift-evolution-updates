import openai
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    client = openai.OpenAI()
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Hello!"}
        ],
        model="gpt-4o"
    )

    print(response.choices[0].message)
