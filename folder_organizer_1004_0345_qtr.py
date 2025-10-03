# 代码生成时间: 2025-10-04 03:45:22
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
Folder Organizer - A Python program using tkinter to organize folder structures.

The program allows users to select a directory and automatically sort files into
subdirectories based on file extensions.
"""

class FolderOrganizer:
    def __init__(self, root):
        # Initialize the GUI with the root window
        self.root = root
        self.root.title('Folder Organizer')
        self.create_widgets()

    def create_widgets(self):
        # Create a button to select the directory
        self.select_button = tk.Button(self.root, text='Select Directory', command=self.select_directory)
        self.select_button.pack()

        # Create a button to organize the files
        self.organize_button = tk.Button(self.root, text='Organize Files', command=self.organize_files, state='disabled')
        self.organize_button.pack()

    def select_directory(self):
        # Use file dialog to select a directory
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.organize_button['state'] = 'normal'
            messagebox.showinfo('Info', 'Directory selected successfully')
        else:
            messagebox.showerror('Error', 'No directory selected')

    def organize_files(self):
        # Organize files in the selected directory
        if not self.directory:
            messagebox.showerror('Error', 'No directory selected')
            return

        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                extension = os.path.splitext(filename)[1]
                if extension:
                    new_dir = os.path.join(self.directory, extension[1:])  # Exclude the dot from the extension
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                    new_file_path = os.path.join(new_dir, filename)
                    try:
                        os.rename(file_path, new_file_path)
                    except OSError as e:
                        messagebox.showerror('Error', f'Error moving file: {e}')
                        return
            else:
                # If the file is not a regular file (e.g., a directory), skip it
                continue

        messagebox.showinfo('Info', 'Files organized successfully')

    def run(self):
        # Run the application
        self.root.mainloop()

# Create the main window and pass it to the FolderOrganizer class
if __name__ == '__main__':
    root = tk.Tk()
    organizer = FolderOrganizer(root)
    organizer.run()