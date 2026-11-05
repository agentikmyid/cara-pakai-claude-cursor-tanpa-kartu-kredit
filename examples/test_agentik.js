import OpenAI from "openai";

// Konfigurasi Client ke Agentik Proxy Gateway
const openai = new OpenAI({
  baseURL: "https://api.agentik.my.id/v1",
  apiKey: "agtk_live_YOUR_API_KEY_HERE", // Dapatkan key di https://agentik.my.id
});

async function main() {
  console.log("Mengirim request ke Agentik API (GPT-4o)...");

  const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: "Kamu adalah AI engineer handal." },
      { role: "user", content: "Jelaskan konsep RAG (Retrieval-Augmented Generation) dalam 3 poin!" }
    ],
  });

  console.log("\nHasil Response:\n");
  console.log(completion.choices[0].message.content);
}

main();
