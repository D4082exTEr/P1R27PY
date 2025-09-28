# 代码生成时间: 2025-09-29 01:47:43
import tkinter as tk
from tkinter import messagebox

# 定义学生画像类
class StudentProfile:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_profile(self):
        """显示学生画像信息"""
        return f"Name: {self.name}
Age: {self.age}
Grade: {self.grade}"

# 定义主窗口类
class StudentProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Profile System")

        # 创建输入字段
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.grade_label = tk.Label(root, text="Grade:")
        self.grade_label.grid(row=2, column=0, padx=10, pady=10)
        self.grade_entry = tk.Entry(root)
        self.grade_entry.grid(row=2, column=1, padx=10, pady=10)

        # 创建显示按钮
        self.display_button = tk.Button(root, text="Display Profile", command=self.display_profile)
        self.display_button.grid(row=3, column=0, columnspan=2, pady=10)

    def display_profile(self):
        try:
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            grade = self.grade_entry.get()

            student = StudentProfile(name, age, grade)
            profile = student.display_profile()
            messagebox.showinfo("Student Profile", profile)
        except ValueError:
            messagebox.showerror("Error", "Invalid age. Please enter a valid integer.")

# 创建主窗口并运行应用
if __name__ == '__main__':
    root = tk.Tk()
    app = StudentProfileApp(root)
    root.mainloop()