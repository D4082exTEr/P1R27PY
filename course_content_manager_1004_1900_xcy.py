# 代码生成时间: 2025-10-04 19:00:43
import tkinter as tk
from tkinter import messagebox

# 课程内容管理程序
class CourseContentManager:
    def __init__(self, master):
        """初始化界面"""
        self.master = master
        self.master.title("课程内容管理")

        # 创建课程名称输入框
        self.course_name_label = tk.Label(master, text="课程名称")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(master)
        self.course_name_entry.pack()

        # 创建课程描述输入框
        self.course_description_label = tk.Label(master, text="课程描述")
        self.course_description_label.pack()
        self.course_description_text = tk.Text(master, height=4, width=50)
        self.course_description_text.pack()

        # 创建添加按钮
        self.add_button = tk.Button(master, text="添加课程", command=self.add_course)
        self.add_button.pack()

        # 创建课程列表
        self.course_listbox = tk.Listbox(master)
        self.course_listbox.pack()

    def add_course(self):
        """添加课程内容"""
        try:
            # 获取输入的课程名称和描述
            course_name = self.course_name_entry.get()
            course_description = self.course_description_text.get("1.0", tk.END)
            
            # 检查输入是否为空
            if not course_name or not course_description:
                messagebox.showerror("错误", "课程名称和描述不能为空")
                return
            
            # 将课程添加到列表框中
            self.course_listbox.insert(tk.END, f"{course_name} - {course_description}")
            
            # 清空输入框
            self.course_name_entry.delete(0, tk.END)
            self.course_description_text.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("错误", str(e))

# 创建主窗口
root = tk.Tk()

# 创建课程内容管理程序实例
app = CourseContentManager(root)

# 运行主循环
root.mainloop()