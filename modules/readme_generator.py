import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_readme_openai(idea):
    prompt = f"""
You are an expert software architect and technical writer.

Generate a detailed GitHub README.md for the following hackathon project idea:

"{idea}"

The README must include:
1. Project Title
2. Problem Statement
3. Solution Description
4. Key Features
5. Use Cases
6. Tech Stack
7. Future Scope
8. Disclaimer

Write the output in professional Markdown.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional technical writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=900
    )

    return response.choices[0].message.content
