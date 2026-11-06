from openai import OpenAI
import os

# Agentik API Quickstart Example
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_YOUR_API_KEY_HERE")  # Dapatkan key di https://agentik.my.id
)

print("Mengirim prompt ke Agentik API (Claude Sonnet)...")

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {"role": "system", "content": "Kamu adalah asisten koding profesional."},
        {"role": "user", "content": "Buatkan script web scraper sederhana dengan Python BeautifulSoup."}
    ]
)

print("\nJawaban AI:\n")
print(response.choices[0].message.content)
