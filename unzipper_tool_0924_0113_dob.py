# 代码生成时间: 2025-09-24 01:13:30
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

"""A simple GUI application for unzipping files using Python and Tkinter."""

class UnzipperTool:
    def __init__(self, root):
        # Initialize the GUI with title and size
        self.root = root
        self.root.title("Unzipper Tool")
        self.root.geometry("400x200")

        # Create a frame for buttons
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Create a button to select the zip file
        select_button = tk.Button(self.frame, text="Select Zip File", command=self.select_zip_file)
        select_button.pack(side=tk.LEFT, padx=10)

        # Create a button to extract the zip file
        extract_button = tk.Button(self.frame, text="Extract Zip File", command=self.extract_zip_file)
        extract_button.pack(side=tk.LEFT, padx=10)

        # Variables to store file path and extract path
        self.zip_file_path = ""
        self.extract_path = ""

    def select_zip_file(self):
        # Open a file dialog to select a zip file
        self.zip_file_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
        if self.zip_file_path:
            messagebox.showinfo("Info", "Zip file selected")
        else:
            messagebox.showwarning("Warning", "No file selected")

    def extract_zip_file(self):
        # Check if a zip file is selected
        if not self.zip_file_path:
            messagebox.showerror("Error", "Please select a zip file first")
            return

        # Ask for the extract path
        self.extract_path = filedialog.askdirectory()
        if not self.extract_path:
            messagebox.showerror("Error", "No extract path selected")
            return

        try:
            # Attempt to extract the zip file
            with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.extract_path)
            messagebox.showinfo("Success", "Zip file extracted successfully")
        except Exception as e:
            # Handle any errors that occur during extraction
            messagebox.showerror("Error", f"Failed to extract zip file: {e}")

# Create the main window and pass it to the UnzipperTool class
if __name__ == "__main__":
    root = tk.Tk()
    app = UnzipperTool(root)
    root.mainloop()