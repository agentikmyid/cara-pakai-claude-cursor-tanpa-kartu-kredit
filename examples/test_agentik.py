from openai import OpenAI

# Agentik API Quickstart Example
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key="agtk_live_YOUR_API_KEY_HERE"  # Dapatkan key di https://agentik.my.id
)

print("Mengirim prompt ke Agentik API (Claude 3.5 Sonnet)...")

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",
    messages=[
        {"role": "system", "content": "Kamu adalah asisten koding profesional."},
        {"role": "user", "content": "Buatkan script web scraper sederhana dengan Python BeautifulSoup."}
    ]
)

print("\nJawaban AI:\n")
print(response.choices[0].message.content)
