# 代码生成时间: 2025-10-10 19:18:36
import tkinter as tk
from tkinter import ttk
from datetime import datetime

"""
一个简单的日期时间选择器程序，使用Python和Tkinter框架。
允许用户选择日期和时间，并将选择的日期时间显示在界面上。
"""

class DateTimeSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('日期时间选择器')
        self.geometry('300x200')

        # 创建日期时间选择器
        self.datetime_var = tk.StringVar()
        self.datetime_var.set(datetime.now().strftime('%Y-%m-%d %H:%M'))

        # 创建日期时间选择器控件
        self.combobox = ttk.Combobox(self, textvariable=self.datetime_var, width=20)
        self.combobox.bind("<Return>", self.on_submit)
        self.combobox.pack(pady=20)

        # 创建提交按钮
        self.submit_button = tk.Button(self, text='提交', command=self.on_submit)
        self.submit_button.pack(pady=10)

    def on_submit(self, event=None):
        """
        处理用户提交的日期时间。
        """
        try:
            # 尝试将输入的字符串转换为datetime对象
            selected_datetime = datetime.strptime(self.datetime_var.get(), '%Y-%m-%d %H:%M')
            print(f'您选择的日期时间是：{selected_datetime}')
        except ValueError:
            print('输入的日期时间格式不正确，请按照“年-月-日 时:分”的格式输入。')

if __name__ == '__main__':
    try:
        app = DateTimeSelector()
        app.mainloop()
    except Exception as e:
        print(f'程序运行出错：{e}')
