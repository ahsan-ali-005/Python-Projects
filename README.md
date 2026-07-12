# 🐍 Python Projects

A collection of beginner-to-intermediate Python projects built while learning core programming concepts, GUI development, API integration, and automation. Each project focuses on a different real-world use case — from a desktop calculator to an AI voice assistant powered by Google Gemini.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Table of Contents

- [About](#-about)
- [Projects](#-projects)
  - [1. Calculator](#1-️-calculator)
  - [2. Jarvis AI Assistant](#2--jarvis-ai-assistant)
  - [3. Image Downloader](#3-️-image-downloader)
  - [4. URL Shortener](#4--url-shortener)
  - [5. Weather App](#5-️-weather-app)
- [Repository Structure](#-repository-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [License](#-license)
- [Contact](#-contact)

---

## 📌 About

This repository is a portfolio of small Python projects, each built to practice a specific skill — GUI design with Tkinter, working with external APIs, file handling, and basic automation. It's part of my ongoing journey into AI/ML and software development.

---

## 🚀 Projects

### 1. 🖩 Calculator

A basic desktop calculator built with **Tkinter** that performs standard arithmetic operations.

**Features:**
- Addition, subtraction, multiplication, and division
- Clear (C) and equals (=) functionality
- Simple, clean GUI interface

**Limitations:**
- No support for advanced/scientific operations (e.g., trigonometry, exponents)
- No keyboard input support (mouse/click only)

**How to run:**
```bash
python Calculator.py
```

**Screenshot:**

> 📸 *[Add your Calculator screenshot here]*

---

### 2. 🤖 Jarvis AI Assistant

A desktop AI assistant powered by the **Google Gemini API**, combining voice recognition and text-to-speech to perform basic tasks and answer questions.

**Features:**
- Understands voice commands using `SpeechRecognition`
- Responds with voice output using `pyttsx3`
- Answers general questions via the Gemini API
- Performs basic automation tasks (e.g., opening YouTube and other websites via `webbrowser`)

**Limitations:**
- Limited to basic tasks — no complex multi-step task automation
- Requires an active internet connection and a valid Gemini API key
- Voice recognition accuracy depends on microphone quality and background noise

**How to run:**
```bash
python Jarvis_AI_Assistant.py
```
> ⚠️ Requires a Google Gemini API key. Add your key in the script before running.

**Screenshot:**

> 📸 *[Add your Jarvis AI Assistant screenshot here]*

---

### 3. 🖼️ Image Downloader

A Tkinter-based image viewer/downloader app that lets users browse through a set of images and save them locally.

**Features:**
- **Next** and **Previous** buttons to browse through images
- **Download** button to save the currently displayed image to the system
- Images are loaded from a local `photos/` folder integrated into the app

**Limitations:**
- Works with a pre-loaded local image set rather than fetching images from the web or an API
- No search or filter functionality

**How to run:**
```bash
python Image_Downloader_App.py
```

**Screenshot:**

> 📸 *[Add your Image Downloader screenshot here]*

---

### 4. 🔗 URL Shortener

A simple GUI-based URL shortener that generates a short link for any long URL entered by the user.

**Features:**
- User enters a long URL and the app generates a corresponding short URL
- Clicking the **Open** button inside the app redirects to the original long URL
- Short URL mappings are stored locally in `data.json`

**Limitations:**
- Does not use a real database or hosting backend — the generated short URL is **not a live/clickable web link** and won't resolve if pasted into a browser
- Redirection only works through the app's own "Open" button, not as a standalone shareable link
- Data is stored locally (`data.json`), not on a server

**How to run:**
```bash
python URL_shortner.py
```

**Screenshot:**

> 📸 *[Add your URL Shortener screenshot here]*

---

### 5. 🌤️ Weather App

A desktop weather application that fetches real-time weather data using the **OpenWeather API**.

**Features:**
- Takes a location (city name) as input from the user
- Fetches and displays current weather information for that location
- Displays the OpenWeather logo (`logo.png`) on the interface

**Limitations:**
- Only shows current weather — no forecast (hourly/weekly) data
- Requires an active internet connection and a valid OpenWeather API key

**How to run:**
```bash
python weather_app.py
```
> ⚠️ Requires an OpenWeather API key. Add your key in the script before running.

**Screenshot:**

> 📸 *[Add your Weather App screenshot here]*

---

## 📁 Repository Structure

| File / Folder | Purpose |
|---|---|
| `Calculator.py` | Source code for the basic Tkinter calculator |
| `Jarvis_AI_Assistant.py` | Source code for the Gemini-powered AI voice assistant |
| `Image_Downloader_App.py` | Source code for the image viewer/downloader app |
| `URL_shortner.py` | Source code for the URL shortener app |
| `weather_app.py` | Source code for the OpenWeather-based weather app |
| `data.json` | Stores mappings of short URLs to their original long URLs (used by URL Shortener) |
| `logo.png` | OpenWeather logo displayed on the Weather App interface |
| `photos/` | Local image set used by the Image Downloader app |
| `.gitignore` | Specifies files/folders excluded from version control |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **GUI:** Tkinter
- **APIs:** Google Gemini API, OpenWeather API
- **Libraries:** `requests`, `speechrecognition`, `pyttsx3`, `webbrowser`, `json`, `pillow`

---

## ⚙️ Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahsan-ali-005/Python-Projects.git
   cd Python-Projects
   ```

2. **Install dependencies**
   ```bash
   pip install requests speechrecognition pyttsx3 pillow
   ```

3. **Add your API keys**
   - Get a [Google Gemini API key](https://ai.google.dev/) for `Jarvis_AI_Assistant.py`
   - Get an [OpenWeather API key](https://openweathermap.org/api) for `weather_app.py`

4. **Run any project**
   ```bash
   python <filename>.py
   ```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and learn from it.

---

## 📬 Contact

**Ahsan Ali**
GitHub: [@ahsan-ali-005](https://github.com/ahsan-ali-005)

⭐ If you found this repository useful, consider giving it a star!
