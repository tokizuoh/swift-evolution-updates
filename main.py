import openai
from dotenv import load_dotenv

from repository import Repository

if __name__ == "__main__":
    load_dotenv()

    repo = Repository()
    proposals = repo.get_recently_changed_proposals()
    for title, content in proposals.items():
        print(f"{title}\n")
        print(content[:1000])
        print("\n" + "=" * 50 + "\n")

    exit()
    # WIP

    client = openai.OpenAI()
    response = client.chat.completions.create(messages=[{"role": "user", "content": "Hello!"}], model="gpt-4o")

    print(response.choices[0].message)
