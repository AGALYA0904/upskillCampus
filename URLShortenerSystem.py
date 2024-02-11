import tkinter as tk
import pyshorteners


# Define colors and fonts
background_color = "#f0f0f0"  # Light gray
text_color = "#333333"  # Dark gray
button_color = "#4CAF50"  # Green
font_family = "Times New Roman"
font_size = 12

def shorten():
    try:
        long_url = longurl_entry.get()
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        shorturl_entry.delete(0, tk.END)  # Clear previous output
        shorturl_entry.insert(0, short_url)
        status_label.config(text="Voila! Your snappy and stylish short URL has been crafted successfully!")
    except Exception as e:	
        status_label.config(text="Error: " + str(e))


root = tk.Tk()
root.title("SnapLinkr")
root.geometry("500x250")
root.configure(bg=background_color)  # Set background color

# Labels and entries
longurl_label = tk.Label(root, text="Unleash your epic link!", bg=background_color, fg=text_color, font=(font_family, font_size))
longurl_entry = tk.Entry(root, bg="#fff", fg=text_color, font=(font_family, font_size))  # White background for entries
shorturl_label = tk.Label(root, text="Your shortened masterpiece!", bg=background_color, fg=text_color, font=(font_family, font_size))
shorturl_entry = tk.Entry(root, bg="#fff", fg=text_color, font=(font_family, font_size))

# Button
shorten_button = tk.Button(root, text="EpicSnap", command=shorten , bg=button_color, fg="white", font=(font_family, font_size))

# Status label
status_label = tk.Label(root, text="Ready to shrink URLs!", bg=background_color, fg=text_color, font=(font_family, font_size))

# Pack widgets
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()
status_label.pack()

root.mainloop()
