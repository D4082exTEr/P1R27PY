# 代码生成时间: 2025-09-24 20:41:08
import tkinter as tk
from tkinter import messagebox
import hashlib

"""
密码加密解密工具是一款基于Python和Tkinter框架的图形用户界面应用，
允许用户输入明文密码，并提供加密和解密功能。
"""

class PasswordEncryptionDecryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title('密码加密解密工具')
        self.create_widgets()

    def create_widgets(self):
        # 输入框
        self.entry_label = tk.Label(self.root, text='输入密码：')
        self.entry_label.pack()
        self.password_entry = tk.Entry(self.root)
        self.password_entry.pack()

        # 加密按钮
        self.encrypt_button = tk.Button(self.root, text='加密', command=self.encrypt)
        self.encrypt_button.pack()

        # 解密按钮
        self.decrypt_button = tk.Button(self.root, text='解密', command=self.decrypt)
        self.decrypt_button.pack()

        # 输出框
        self.result_label = tk.Label(self.root, text='')
        self.result_label.pack()

    def encrypt(self):
        # 获取输入的密码
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning('警告', '密码不能为空！')
            return

        # 加密密码
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        self.result_label.config(text=f'加密结果：{encrypted_password}')

    def decrypt(self):
        # 获取输入的密码
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning('警告', '密码不能为空！')
            return

        # 注意：SHA-256是单向加密，无法解密
        messagebox.showinfo('提示', 'SHA-256是单向加密，不支持解密操作。')

if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordEncryptionDecryptionApp(root)
    root.mainloop()