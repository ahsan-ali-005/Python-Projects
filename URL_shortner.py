from tkinter import *
import string, random
import webbrowser
import json
import pyperclip

def copy_to_clip(text):
    pyperclip.copy(text)
    error_label.config(text="Copied to clipboard!", fg="lightgreen")

def shorten_url(long_url):
    global data
    
    # Clean up any previous result button if it exists
    if 'result_btn' in globals() and result_btn.winfo_exists():
        result_btn.destroy()

    if long_url == "" or not (long_url.startswith("https://") or long_url.startswith("http://")):
        error_label.config(text="Please Enter a Valid URL!", fg="red")
        return

    # Check if URL already exists
    if long_url in data.values():
        error_label.config(text="URL already shortened!", fg="yellow")
        # Find the short URL key matching the long URL value
        short_url = [k for k, v in data.items() if v == long_url][0]
        create_result_button(short_url)
    else:
        # Generate new short URL
        rd_characters = "".join(random.choice(characters) for _ in range(6))
        short_url = f"https://short.ly/{rd_characters}"
        
        data[short_url] = long_url
        with open("data.json", "w") as f:
            json.dump(data, f)
            
        error_label.config(text="URL Shortened Successfully!", fg="green")
        create_result_button(short_url)

def create_result_button(short_url):
    global result_btn
    # Clicking this button will now copy it AND try to open the original long URL
    result_btn = Button(root, text=short_url, background="white", fg="black", 
                        font=("verdana", 10, "underline"),
                        command=lambda: handle_url_click(short_url))
    result_btn.pack(pady=10)

def handle_url_click(short_url):
    copy_to_clip(short_url)
    # Open the actual destination URL in the browser
    webbrowser.open(data[short_url])

# Initialize Data
characters = string.ascii_letters + string.digits
data = {}
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except Exception as e:
    print("No existing data found, starting fresh:", e)

# UI Setup
root = Tk()
root.geometry("350x400")
root.resizable(0, 0)
root.config(background="black")
root.title("URL SHORTENER")

instruction = Label(root, text="ENTER LONG URL HERE:", fg="white", background="black", font=("verdana", 12, "bold"))
instruction.pack(pady=(50, 2))

long_url_entry = Entry(root, width=35)
long_url_entry.pack(padx=10, pady=15)

btn = Button(root, text="Get Short URL!", font=("verdana", 10, "bold"), command=lambda: shorten_url(long_url_entry.get().strip()))
btn.pack(pady=8)

# Single reusable error/status label
error_label = Label(root, text="", background="black", fg="white", font=("verdana", 10))
error_label.pack(pady=10)

root.mainloop()