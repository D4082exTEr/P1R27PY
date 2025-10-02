# 代码生成时间: 2025-10-02 17:49:34
import tkinter as tk
from tkinter import messagebox

"""
项目管理工具，使用TKINTER框架创建GUI应用程序。
"""

class ProjectManagementTool:
    def __init__(self, root):
        """
        初始化项目管理工具。
        :param root: 应用程序的根窗口
        """
        self.root = root
        self.root.title("项目管理工具")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        """
        创建GUI组件。
        """
        self.project_list = tk.Listbox(self.root)
        self.project_list.pack(pady=10)

        self.add_button = tk.Button(self.root, text="添加项目", command=self.add_project)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="删除项目", command=self.remove_project)
        self.remove_button.pack(pady=5)

    def add_project(self):
        """
        添加新项目到列表。
        """
        project_name = simpledialog.askstring("输入", "输入项目名称：")
        if project_name:
            self.project_list.insert(tk.END, project_name)
        else:
            messagebox.showwarning("警告", "项目名称不能为空")

    def remove_project(self):
        """
        从列表中删除选定的项目。
        """
        selected_index = self.project_list.curselection()
        if selected_index:
            self.project_list.delete(selected_index)
        else:
            messagebox.showwarning("警告", "请选择要删除的项目")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectManagementTool(root)
    root.mainloop()
