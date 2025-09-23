# 代码生成时间: 2025-09-23 08:18:32
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import json
"""
Data Backup and Restore Application using Python and Tkinter
This application provides a simple GUI to backup and restore data from a specified directory.
"""

class DataBackupRestoreApp:
    def __init__(self, root):
        # Set the title of the window
        self.root = root
        self.root.title('Data Backup and Restore')

        # Set the geometry of the window
        self.root.geometry('400x200')

        # Create a Label
        self.label = tk.Label(self.root, text='Select a directory for backup or restore:', font=('Arial', 12))
        self.label.pack(pady=10)

        # Create an Entry widget to display the selected directory
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)

        # Create a Button to open the file dialog for directory selection
        self.browse_button = tk.Button(self.root, text='Browse', command=self.browse_directory)
        self.browse_button.pack(pady=5)

        # Create a Button to backup the data
        self.backup_button = tk.Button(self.root, text='Backup Data', command=self.backup_data)
        self.backup_button.pack(pady=5)

        # Create a Button to restore the data
        self.restore_button = tk.Button(self.root, text='Restore Data', command=self.restore_data)
        self.restore_button.pack(pady=5)

    def browse_directory(self):
        """Open a file dialog to select a directory."""
        directory = filedialog.askdirectory()
        if directory:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, directory)

    def backup_data(self):
        """Backup the data from the selected directory."""
        directory = self.entry.get()
        if not directory:
            messagebox.showerror('Error', 'Please select a directory')
            return

        # Create a backup directory with a timestamp
        backup_dir = os.path.join(directory, 'backup_' + time.strftime('%Y%m%d%H%M%S'))
        os.makedirs(backup_dir, exist_ok=True)

        try:
            # Copy all files from the original directory to the backup directory
            for item in os.listdir(directory):
                s = os.path.join(directory, item)
                d = os.path.join(backup_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
            messagebox.showinfo('Success', 'Data backed up successfully')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def restore_data(self):
        """Restore the data to the selected directory."""
        directory = self.entry.get()
        if not directory:
            messagebox.showerror('Error', 'Please select a directory')
            return

        # Find all backup directories in the selected directory
        backup_dirs = [d for d in os.listdir(directory) if d.startswith('backup_')]
        if not backup_dirs:
            messagebox.showerror('Error', 'No backup data found')
            return

        # Prompt the user to select a backup directory
        backup_dir = filedialog.askdirectory(title='Select a backup directory',
                                            initialdir=os.path.join(directory, backup_dirs[0]))
        if not backup_dir:
            return

        try:
            # Copy all files from the backup directory to the original directory
            for item in os.listdir(backup_dir):
                s = os.path.join(backup_dir, item)
                d = os.path.join(directory, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            messagebox.showinfo('Success', 'Data restored successfully')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()

    # Create an instance of the DataBackupRestoreApp class
    app = DataBackupRestoreApp(root)

    # Start the main event loop
    root.mainloop()