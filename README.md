# 🎧 AI Street Interview – World Happiness Report 2019

This project is a continuation of **Task 05: Descriptive Statistics with LLMs**, evolving into a creative AI audio simulation using `gTTS` and Python. It generates a podcast-style interview where "Claude" (an AI assistant) answers descriptive and complex questions based on the **World Happiness Report 2019**.

---

## 🎯 Objective

To simulate a realistic data storytelling experience by:
- Generating **Q&A dialogue** based on a real dataset.
- Converting that into **voiceover audio clips** using `gTTS`.
- Producing a final **merged interview audio file**.
- Documenting the process in a reproducible and educational format.

---

## 🧠 Dataset Overview

- **Source:** World Happiness Report 2019
- **Countries:** 156
- **Features:** GDP per capita, social support, life expectancy, freedom, generosity, perceptions of corruption, happiness score
- **Format Used:** `.csv` (refer to Task 05)

---

## 💬 Interview Structure

- Total Q&A Pairs: 18 (divided into simple + complex)
- Format: `(Speaker, Dialogue)` used to generate `mp3` files
- Speakers: `Interviewer`, `Claude`

Example:

```python
("Interviewer", "How many countries are represented in this dataset?"),
("Claude", "The dataset includes 156 countries."),
```

---

## 🗣️ Tools Used

| Tool     | Purpose                                 |
|----------|------------------------------------------|
| `gTTS`   | Convert text lines to voice (.mp3)       |
| `os`     | Create directories and save files        |
| `shutil` | Merge mp3 files without needing ffmpeg   |

---

## 📁 Folder Structure

```bash
Task_06_Claude_Interview/
│
├── outputs/
│   ├── audio/                    # Individual Q&A .mp3 files
│   └── interview_audio.mp3       # Final combined interview audio
│
├── generate_audio.py             # Full audio generation script (no ffmpeg required)
├── requirements.txt              # Project dependencies
└── README.md                     # This file
```

---

## 🧪 How to Run

1. ✅ Create and activate your virtual environment.
2. ✅ Install dependencies:

```bash
pip install -r requirements.txt
```

3. ✅ Run the script:

```bash
python generate_audio.py
```

4. 🎧 Check the `outputs/` folder for the final interview.

---

## 🧾 Output Example

- `outputs/audio/line_00_Interviewer.mp3`
- `outputs/audio/line_01_Claude.mp3`
- ...
- `outputs/interview_audio.mp3` ✅ Final result

---

## 🤖 Use of Generative AI

Parts of this project were developed with the assistance of **ChatGPT (GPT-4)**, including:

- Structuring and drafting the interview Q&A script based on descriptive statistics from the *World Happiness Report 2019* dataset.
- Writing Python code to generate voiceovers using `gTTS`, organize output files, and streamline the audio generation pipeline.
- Providing formatting templates for documentation (`README.md`, workflow summaries, etc.).

This aligns with prior AI-assisted work done in **Task 05**, where ChatGPT was used for prompt engineering and validation script scaffolding.

All generated content was reviewed and manually refined by the student for clarity, accuracy, and educational alignment.

---

## 📌 Notes

- This version avoids `ffmpeg` by using `shutil` to concatenate audio.
- Final `.mp3` plays like a conversation with alternating speaker voices.

---

## ✨ Author

- **Name:** Yaswanth LalpetVari
- **Task:** 06 – AI Audio Interview (Claude Explains Descriptive Stats)
- **University:** Syracuse University