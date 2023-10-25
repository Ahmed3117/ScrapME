import os
import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk, filedialog, messagebox
import webbrowser
from scrapdata import scrapurl
from exportdatatoexcelfile import storescrapeddatatoexcel
from downloadimagesfromexcel import downloadimages

def browse_path():
    default_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    path = filedialog.askdirectory()  # Open a directory selection dialog
    if path:
        output_label.config(text=f"Selected path: {path}")
    else:
        path = default_path
        output_label.config(text=f"Selected path: {path}")




def runner():
    urls = urls_text.get("1.0", "end-1c").split('\n')[:-1]
    code = int(code_entry.get())
    path = output_label.cget("text").replace("Selected path: ", "")
    print(urls)

    try:
        storescrapeddatatoexcel(urls, path)
        file_path = path + '/scraped_data.xlsx'
        print(file_path)
        print("lllllllllllllllllllllllllllllllllllllllllllllllllll")
        downloadimages(file_path, code)

        # Create a custom message box with a clickable link
        message = "Task completed successfully."
        link_message = "Click OK to open the result location: {}".format(os.path.dirname(file_path))
        result = messagebox.showinfo("Success", message, detail=link_message)

        # If the result is "ok" and the link was clicked, open the file path
        if result == "ok":
            webbrowser.open(os.path.dirname(file_path))
        # Display a message when the task ends correctly
        # messagebox.showinfo("Task Completed", "Done correctly. Click the link below to access the file:\n" + os.path.dirname(file_path))
    except Exception as e:
        messagebox.showerror("Task Error", f"An error occurred: {str(e)}")


root = tk.Tk()
root.title("Scraper")  # Title for the window

# Set window icon
# icon = PhotoImage(file="scraper.png")  # Replace "your_icon.png" with your icon file
# root.iconphoto(True, icon)

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
title_label = ttk.Label(root, text="ScrapMe", font=('Arial', 16, 'bold'), foreground='#0074a0')
title_label.grid(row=0, column=0, padx=10, pady=10)

# Labels for URLs and code
urls_label = ttk.Label(main_frame, text="URLs:")
urls_label.grid(row=0, column=0, sticky='w')

code_label = ttk.Label(main_frame, text="image code:")
code_label.grid(row=1, column=0, sticky='w')

# Text widget for multiple URLs
urls_text = tk.Text(main_frame, height=10, width=60,relief='flat')
urls_text.grid(row=0, column=1, padx=5, pady=5)

code_entry = ttk.Entry(main_frame, width=60)
code_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to start the process
start_button = ttk.Button(main_frame, text="Start", command=runner)
start_button.grid(row=2, column=1, pady=10)

# Label for displaying the output
output_label = ttk.Label(main_frame, text="",foreground='#000000', font=('Arial', 12))
output_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='w')
# Button to browse for a directory
browse_button = ttk.Button(main_frame, text="Browse", command=browse_path)
browse_button.grid(row=2, column=0, pady=10)


root.mainloop()






