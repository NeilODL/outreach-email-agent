import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

GITHUB_URL = "https://github.com/NeilODL"

def generate_email(contact):
    prompt = f"""
Write a concise, natural cold email to the recruitment address of {contact['company_name']}. 

Tone: honest, warm, and professional — no fluff, no buzzwords, no exaggeration.

Context:
- I'm Neil, a recent Financial Mathematics master's grad.
- I did an AI internship where I built AI Agents for a startup in Barcelona.
- I came across {contact['company_name']} and their work on: {contact['company_info']} (At this point you dont have to use the exact wording, find a wording that sounds right, so you dont ahve to write it all out if thats unnatural)
- I’m curious if there are any junior AI/ML roles I might contribute to — I'm UK-based and open to remote work.
- I've attached my CV. My GitHub is here: {GITHUB_URL}
- This message was sent via a small outreach agent I built — just a simple example of what I enjoy working on.

Keep it short (max 120 words). Avoid formal phrases like "I was genuinely intrigued" or "I'm truly passionate." Just be clear and humanized. End with: “Best, Neil”
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    return response.choices[0].message.content.strip()
