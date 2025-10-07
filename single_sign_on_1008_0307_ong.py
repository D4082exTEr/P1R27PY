# 代码生成时间: 2025-10-08 03:07:22
import tkinter as tk
from tkinter import messagebox

"""
Single Sign-On (SSO) system using Python and Tkinter.
This simple system allows users to log in with a username and password.
For demonstration purposes, it uses hardcoded credentials.
In a real-world scenario, you would integrate with a database or authentication service.
"""

# Constants for hardcoded credentials
USERNAME = 'admin'
PASSWORD = 'password123'

class SSOSystem:
    """Class representing the Single Sign-On system."""
    def __init__(self, root):
        """Initialize the SSO system with the Tkinter root window."""
        self.root = root
        self.root.title('Single Sign-On System')
        self.create_widgets()

    def create_widgets(self):
        """Create the user interface widgets."""
        # Username label and entry
        tk.Label(self.root, text='Username:').grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        tk.Label(self.root, text='Password:').grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login button
        login_button = tk.Button(self.root, text='Login', command=self.login)
        login_button.grid(row=2, column=1, padx=10, pady=10)

    def login(self):
        """Attempt to log in the user with the provided credentials."""
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        try:
            # Simple credential check for demonstration
            if entered_username == USERNAME and entered_password == PASSWORD:
                messagebox.showinfo('Login Successful', 'You have successfully logged in!')
            else:
                messagebox.showerror('Login Failed', 'Invalid username or password.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

def main():
    """Main function to start the SSO system."""
    root = tk.Tk()
    sso_system = SSOSystem(root)
    root.mainloop()

if __name__ == '__main__':
    main()