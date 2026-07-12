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

This repository is a portfolio of my small Python projects, each built to practice a specific skill — GUI design with Tkinter, working with external APIs, file handling, and basic automation. It's part of my ongoing journey into AI/ML and software development.

---

## 🚀 Projects

### 1. 🖩 Calculator

A basic desktop calculator built with **Tkinter** that performs standard arithmetic operations.

**Features:**
- Addition, subtraction, multiplication, and division
- Clear (C) and equals (=) functionality
- Simple, clean GUI interface


**How to run:**
```bash
python Calculator.py
```


<img width="202" height="306" alt="image" src="https://github.com/user-attachments/assets/26cbffa8-88f0-4faa-ba67-c996e295ad2b" />


---

### 2. 🤖 Jarvis AI Assistant

A desktop AI assistant powered by the **Google Gemini API**, combining voice recognition and text-to-speech to perform basic tasks and answer questions.

**Features:**
- Understands voice commands using `SpeechRecognition`
- Responds with voice output using `pyttsx3`
- Answers general questions via the Gemini API
- Performs basic automation tasks (e.g., opening YouTube and other websites via `webbrowser`)


**How to run:**
```bash
python Jarvis_AI_Assistant.py
```
> ⚠️ Requires a Google Gemini API key. Add your API key in the script before running.

<img width="1139" height="585" alt="image" src="https://github.com/user-attachments/assets/a6136a60-14fb-4206-8bb0-aca9e9720c4b" />


---

### 3. 🖼️ Image Downloader

A Tkinter-based image viewer/downloader app that lets users browse through a set of images and save them locally.

**Features:**
- **Next** and **Previous** buttons to browse through images
- **Download** button to save the currently displayed image to the system
- Images are loaded from a local `photos/` folder integrated into the app


**How to run:**
```bash
python Image_Downloader_App.py
```

<img width="255" height="317" alt="image" src="https://github.com/user-attachments/assets/b79ed019-70fe-481f-b324-7787f0295abb" />


---

### 4. 🔗 URL Shortener

A simple GUI-based URL shortener that generates a short link for any long URL entered by the user.

**Features:**
- User enters a long URL and the app generates a corresponding short URL
- Clicking the **Open** button inside the app redirects to the original long URL
- Short URL mappings are stored locally in `data.json`


**How to run:**
```bash
python URL_shortner.py
```

<img width="260" height="311" alt="image" src="https://github.com/user-attachments/assets/5077353a-fc37-452b-9c2b-c9916399c41f" />


---

### 5. 🌤️ Weather App

A desktop weather application that fetches real-time weather data using the **OpenWeather API**.

**Features:**
- Takes a location (city name) as input from the user
- Fetches and displays current weather information for that location
- Displays the OpenWeather logo (`logo.png`) on the interface


**How to run:**
```bash
python weather_app.py
```
> ⚠️ Requires an OpenWeather API key. Add your API key in the script before running.

<img width="742" height="717" alt="image" src="https://github.com/user-attachments/assets/2f087558-cdf7-4cff-aef3-b55c23ad5660" />


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
