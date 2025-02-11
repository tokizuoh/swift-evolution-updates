import os
from datetime import datetime

import openai
import pytz
from dotenv import load_dotenv

from repository import Repository


def load_prompt():
    with open("prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def save_summary(file_path, markdown_text):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)


if __name__ == "__main__":
    load_dotenv()

    repo = Repository()
    proposals = repo.get_recently_changed_proposals()

    prompt_template = load_prompt()

    client = openai.OpenAI()

    jst = pytz.timezone("Asia/Tokyo")
    today_jst = datetime.now(jst).strftime("%Y/%m/%d")
    markdown_output = "# {}".format(today_jst)
    markdown_output += "\n\n"

    for _, content in proposals.items():
        prompt = prompt_template.replace("{プロポーザルの原文}", content)
        response = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="gpt-4o")

        summary = response.choices[0].message.content

        markdown_output += summary + "\n\n"

    year = datetime.now(jst).strftime("%Y")
    output_dir = f"docs/{year}"
    os.makedirs(output_dir, exist_ok=True)

    date_str = datetime.now(jst).strftime("%Y%m%d")
    file_path = f"{output_dir}/{date_str}.md"

    save_summary(file_path, markdown_output)
