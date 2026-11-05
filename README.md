# ⚡ Cara Menggunakan Claude 3.5 Sonnet & GPT-4o di Cursor / Cline Tanpa Kartu Kredit

[![Website](https://img.shields.io/badge/Website-agentik.my.id-0070f3?style=flat-square&logo=cloudflare&logoColor=white)](https://agentik.my.id)
[![Payment](https://img.shields.io/badge/Pembayaran-QRIS%20Instan-E31E24?style=flat-square)](https://agentik.my.id)
[![Endpoint](https://img.shields.io/badge/Endpoint-OpenAI%20Compatible-00A67E?style=flat-square&logo=openai&logoColor=white)](https://agentik.my.id)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

Panduan komprehensif integrasi API AI model mutakhir (**Claude 3.5 Sonnet, GPT-4o, Gemini 1.5, DeepSeek R1**) untuk developer, mahasiswa, dan AI builder Indonesia tanpa kendala kartu kredit luar negeri yang sering ditolak atau biaya langganan bulanan yang mahal.

Solusi gateway resmi: **[Agentik.my.id](https://agentik.my.id)**

---

## 📌 Daftar Isi
1. [Latar Belakang Masalah](#-latar-belakang-masalah)
2. [Solusi dengan Agentik API](#-solusi-dengan-agentik-api)
3. [Panduan Integrasi Cursor IDE](#-panduan-integrasi-cursor-ide)
4. [Panduan Integrasi VS Code (Cline / Roo Code)](#-panduan-integrasi-vs-code-cline--roo-code)
5. [Contoh Kode Integrasi (Python & Node.js)](#-contoh-kode-integrasi)
6. [Tabel Model yang Didukung](#-tabel-model-yang-didukung)
7. [FAQ & Troubleshooting](#-faq--troubleshooting)

---

## 🛑 Latar Belakang Masalah
Banyak developer dan AI enthusiast di Indonesia menghadapi kendala saat ingin memanfaatkan AI coding assistant:
1. **Kartu Debit/Kredit Ditolak:** Bank lokal (BCA, Mandiri, Jenius, Jago, BNI) sering memblokir pembayaran berulang (recurring billing) Anthropic / OpenAI karena sistem 3D-Secure.
2. **Komitmen Biaya Bulanan Berat:** Langganan $20/bulan di Anthropic Pro atau ChatGPT Plus terasa mubazir jika kita hanya coding di akhir pekan atau proyek sampingan.
3. **Pajak & Kurs Siluman:** Transaksi valuta asing dikenakan biaya konversi bank yang cukup tinggi.

---

## 💡 Solusi dengan Agentik API
**[Agentik.my.id](https://agentik.my.id)** hadir sebagai jembatan resmi (AI API Proxy Gateway):
* **Cukup Scan QRIS:** Top-up saldo mulai dari nominal kecil (GoPay, OVO, DANA, BCA, Livin, ShopeePay).
* **Pay-as-you-go:** Saldo hanya terpotong per token yang benar-benar Anda gunakan. Tidak ada biaya bulanan.
* **100% OpenAI-Compatible:** Format endpoint standar industri. Tinggal ganti `Base URL` dan `API Key`.

---

## 🖥️ Panduan Integrasi Cursor IDE

Cursor adalah AI-first Code Editor terpopuler saat ini. Anda bisa menghubungkan Cursor langsung ke endpoint Agentik:

### Langkah-langkah:
1. Buka **Cursor IDE**.
2. Masuk ke menu **Settings** (`Ctrl + ,` di Windows/Linux atau `Cmd + ,` di Mac).
3. Di panel kiri, klik tab **Models**.
4. Aktifkan saklar **OpenAI API Key**.
5. Klik **Override OpenAI Base URL**, lalu masukkan:
   ```text
   https://api.agentik.my.id/v1
   ```
6. Masukkan API Key yang Anda dapatkan dari dashboard **[Agentik.my.id](https://agentik.my.id)** (format: `agtk_live_...`).
7. Tambahkan model yang ingin digunakan jika belum muncul di daftar:
   * `claude-3-5-sonnet-20241022`
   * `gpt-4o`
   * `deepseek-chat`
8. Selesai! Tekan `Ctrl + K` atau `Ctrl + L` di file kodingan Anda untuk langsung mulai coding dengan AI.

---

## 💻 Panduan Integrasi VS Code (Cline / Roo Code)

Ekstensi **Cline** (Autonomous Coding Agent) di VS Code sangat powerful jika dipasangkan dengan Claude 3.5 Sonnet via Agentik:

1. Buka VS Code dan klik ikon ekstensi **Cline** di bilah sisi.
2. Klik ikon **Settings** (roda gigi) di bagian atas panel Cline.
3. Pada opsi **API Provider**, pilih: `OpenAI Compatible`.
4. Masukkan konfigurasi berikut:
   - **Base URL:** `https://api.agentik.my.id/v1`
   - **API Key:** `agtk_live_your_api_key_here`
   - **Model ID:** `claude-3-5-sonnet-20241022`
5. Klik **Save Changes**. Cline sekarang siap membuat file, membaca bug, dan memperbaiki aplikasi Anda secara otonom!

---

## 👨‍💻 Contoh Kode Integrasi

### 1. Python (`pip install openai`)
```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key="agtk_live_your_api_key_here"  # Ganti dengan key Agentik Anda
)

response = client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",
    messages=[
        {"role": "user", "content": "Tuliskan fungsi Python untuk menghitung Fibonacci dengan memoization."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

### 2. Node.js / TypeScript (`npm install openai`)
```javascript
import OpenAI from "openai";

const openai = new OpenAI({
  baseURL: "https://api.agentik.my.id/v1",
  apiKey: "agtk_live_your_api_key_here",
});

async function main() {
  const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: "Halo dari developer Indonesia!" }],
  });

  console.log(completion.choices[0].message.content);
}

main();
```

---

## 📊 Tabel Model yang Didukung

| Model Name | Model ID di Agentik | Keunggulan Utama |
| :--- | :--- | :--- |
| **Claude 3.5 Sonnet** | `claude-3-5-sonnet-20241022` | Raja coding, arsitektur software, dan penulisan logic presisi |
| **GPT-4o** | `gpt-4o` | Multimodal cepat, penalaran umum, integrasi luas |
| **Gemini 1.5 Pro** | `gemini-1.5-pro` | Konteks window raksasa hingga 1-2 juta token |
| **DeepSeek R1 / V3** | `deepseek-reasoner` / `deepseek-chat` | Penalaran matematis & algoritma dengan efisiensi biaya luar biasa |

---

## ❓ FAQ & Troubleshooting

**Q: Apakah API Key dari Agentik aman?**  
A: Sangat aman. Seluruh request ditransmisikan via HTTPS terenkripsi langsung ke inference server resmi tanpa pencatatan prompt pribadi Anda.

**Q: Berapa minimal top up saldo?**  
A: Sangat terjangkau, mulai dari Rp10.000 via QRIS tanpa potongan biaya siluman.

**Q: Apakah bisa untuk agent seperti AutoGen atau CrewAI?**  
A: Ya! Karena Agentik 100% mengikuti spesifikasi OpenAI API, framework agentik apa pun yang mendukung custom `base_url` dapat langsung berjalan lancar.

---

## 🚀 Mulai Sekarang
Daftar akun dan klaim akses API Anda dalam 1 menit:  
👉 **[https://agentik.my.id](https://agentik.my.id)**

---
*Tags / Kata Kunci: cursor ai indonesia, claude 3.5 sonnet tanpa kartu kredit, bayar api openai qris, alternatif openrouter indonesia, tutorial cline vscode, agentik proxy ai.*
