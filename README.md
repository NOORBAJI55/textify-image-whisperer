# Textify: The Image Whisperer 🎤

A lightweight Python-based CLI tool that extracts text from images using **Tesseract OCR** and converts it into **speech** using **gTTS**, or saves it as a **text file**. Perfect for converting handwritten notes, documents, or signs into digital formats.

---

## 🚀 Features

- 📷 Extract text from any image using `pytesseract`
- 🔊 Convert extracted text into audio using `gTTS`
- 📝 Save the text as a `.txt` file
- 🎧 Save the speech as a `.mp3` file
- 🧠 Intelligent timestamped filenames
- 🎨 Colored console output for better UX with `colorama`

---

## 📦 Requirements

Make sure you have the following installed:

```bash
pip install pytesseract gTTS pillow colorama
