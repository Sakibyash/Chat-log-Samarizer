# AI Chat Log Summarizer

![Project Banner](screenshots/banner.png)

The **AI Chat Log Summarizer** is a Python-based tool designed to parse, analyze, and summarize AI chat logs from `.txt` files. Built with robust text-processing techniques like TF-IDF and frequency-based keyword extraction, it efficiently delivers concise summaries and insightful statistics from user-AI conversations.

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Screenshots](#screenshots)
- [License](#license)
- [Contact](#contact)

---

## 📖 Overview

This project fulfills a practical need for summarizing long AI-human interaction logs. It reads chat files with clear "User:" and "AI:" indicators, counts messages, identifies core discussion topics, and saves summaries for reporting or archival purposes. 

Bonus capabilities include batch processing and keyword extraction using TF-IDF for higher precision.

---

## 🚀 Features

- ✅ **Chat Parsing** — Detects and processes lines prefixed with `User:` or `AI:`.
- 📊 **Message Statistics** — Total messages, user/AI-specific counts.
- 🧠 **Keyword Extraction** — Top 5 keywords using TF-IDF or frequency-based analysis.
- 📝 **Summary Generation** — Outputs a clean summary with key insights.
- 📂 **Batch Mode** — Processes all chat files in a folder.
- 💥 **Error Handling** — Manages missing files or bad inputs gracefully.
- 🔁 **Reusable Code** — Organized, modular, and class-based.
- 📚 **Beginner-Friendly** — Well-documented and easy to run.

---

## 📁 Project Structure

AI-Chat-Log-Summarizer/
├── src/
│ ├── init.py
│ └── chat_parser.py
├── data/
│ └── sample_chat_1.txt
├── output/
│ └── summary_1.txt
├── screenshots/
│ ├── terminal_output.png
│ ├── output_file.png
│ └── project_structure.png
├── requirements.txt
├── LICENSE
└── README.md

yaml
Copy
Edit

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- pip

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/AI-Chat-Log-Summarizer.git
cd AI-Chat-Log-Summarizer

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
🧪 Usage
Run for a single file
bash
Copy
Edit
python src/chat_parser.py
Run batch mode in Python
python
Copy
Edit
from src.chat_parser import ChatLogSummarizer

summarizer = ChatLogSummarizer(use_tfidf=True)
summarizer.process_folder("data/", "output/")
Optional CLI (if implemented)
bash
Copy
Edit
python src/chat_parser.py --file data/sample_chat_1.txt --output output/ --tfidf
python src/chat_parser.py --folder data/ --output output/ --tfidf
🧾 Sample Output
📥 Input (data/sample_chat_1.txt)
vbnet
Copy
Edit
User: What is Python used for?
AI: Python is used for web development, data science, automation, and more.
User: Can Python handle big data?
AI: Yes, with libraries like Pandas and Spark, Python is great for big data.
User: How does AI work with Python?
AI: AI in Python uses libraries like TensorFlow and PyTorch for machine learning.
📤 Output (output/summary_1.txt)
yaml
Copy
Edit
Chat Log Summary:
- Total exchanges: 6
- User messages: 3
- AI messages: 3
- Main topics discussed: python, data, ai, libraries, development
- Top keywords: python, data, ai, libraries, development
🖼️ Screenshots
1. Terminal Output


2. Output Summary File


3. Project Folder Structure


📄 License
This project is licensed under the MIT License.

📬 Contact
Name: MD. Sakib Hasan
Email: sakibyash@gmail.com
GitHub: Sakibyash

