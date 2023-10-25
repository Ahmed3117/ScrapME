import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import filedialog

from scrapdata import scrapurl
from exportdatatoexcelfile import storescrapeddatatoexcel
from downloadimagesfromexcel import downloadimages

def browse_path():
    path = filedialog.askdirectory()  # Open a directory selection dialog
    if path:
        output_label.config(text=f"Selected path: {path}")

def runner():
    urls = urls_text.get("1.0", "end-1c").split('\n')[:-1]
    code = int(code_entry.get())
    path = output_label.cget("text").replace("Selected path: ", "")  # Get the selected path
    print(urls)
    # print(code)
    # print(path)
    # output_label.config(text="Processing... URLs: {}, Code: {}, Path: {}".format(", ".join(urls), code, path))
    storescrapeddatatoexcel(urls,path)
    file_path = path + '/scraped_data.xlsx'
    print(file_path)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
    downloadimages(file_path,code)

root = tk.Tk()
root.title("Scraper")  # Title for the window

# Set window icon
icon = PhotoImage(file="scraper.png")  # Replace "your_icon.png" with your icon file
root.iconphoto(True, icon)

# Create a style for buttons
style = ttk.Style()
style.configure('TButton', foreground='#0074a0', background='#000000', font=('Arial', 12))
style.map('TButton', background=[('active', '#005d8c')])

# Create a style for labels
style.configure('TLabel', font=('Arial', 12), foreground='#0074a0')  # labels

# Create a style for entry fields
style.configure('TEntry', font=('Arial', 12))

# Create a style for the main frame
style.configure('TFrame', background='#f0f0f0', relief='ridge', borderwidth=2)

# Create and configure the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Title and description
title_label = ttk.Label(root, text="Web Scraper Application", font=('Arial', 16, 'bold'), foreground='#0074a0')
title_label.grid(row=0, column=0, padx=10, pady=10)

# Labels for URLs and code
urls_label = ttk.Label(main_frame, text="Enter URLs (comma separated links):")
urls_label.grid(row=0, column=0, sticky='w')

code_label = ttk.Label(main_frame, text="Enter code (to name images):")
code_label.grid(row=1, column=0, sticky='w')

# Text widget for multiple URLs
urls_text = tk.Text(main_frame, height=6, width=40)
urls_text.grid(row=0, column=1, padx=5, pady=5)

code_entry = ttk.Entry(main_frame, width=40)
code_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to start the process
start_button = ttk.Button(main_frame, text="Start", command=runner)
start_button.grid(row=2, column=1, pady=10)

# Label for displaying the output
output_label = ttk.Label(main_frame, text="", font=('Arial', 12))
output_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='w')
# Button to browse for a directory
browse_button = ttk.Button(main_frame, text="Browse", command=browse_path)
browse_button.grid(row=2, column=0, pady=10)

# Label for displaying the selected path
output_label = ttk.Label(main_frame, text="", font=('Arial', 12))
output_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='w')

root.mainloop()






